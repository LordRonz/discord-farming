import asyncio

async def main():
    try:
        import pyautogui
        import time
        from random import choice
        import nhentaigen.nhentai_code_generator as nh
        from pyperclip import copy as cpy
        from utils.argparser import get_args
        from utils.read_txt import get_txt, get_copypasta

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.3

        NHENTAI, TEXT, COPYPASTA = 0, 1, 2

        flags = get_args()

        txt = get_txt(flags['s'])
        copypasta = None
        if not txt:
            copypasta = get_copypasta(flags['s'])

        state = NHENTAI
        if txt:
            state = TEXT
        elif copypasta:
            state = COPYPASTA

        # Initial delay
        time.sleep(flags['i'])

        if state == NHENTAI:
            if not nh.fetch_latest():
                print('Error connecting to nhentai!')
                print('TXT mode')
                path = choice(('./uzumakibayu.txt', './shakespeare.txt', './potterspells.txt'))
                with open(path) as f:
                    txt = f.read().splitlines()

        if flags['l']:
            width, height = pyautogui.size()
            # posx, posy = 0.3140625 * width, 0.95 * height
            loc = pyautogui.locateOnScreen('ss.png', grayscale=True)
            if loc:
                posx, posy = pyautogui.center(loc)
                pyautogui.moveTo(posx, posy)
                pyautogui.click()

        delay = max(50.69, flags['d'])
        ## PLACE CURSOR IN THE TEXT BOX

        async def nh_mode():
            nhcode = nh.valid_url()
            while True:
                s = await nhcode
                cpy(s)
                await asyncio.sleep(0.69)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                await asyncio.sleep(1)
                if flags['r']:
                    pyautogui.press('a')
                    pyautogui.press('backspace')
                    pyautogui.press('up')
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.press('backspace')
                    pyautogui.press('enter')
                    await asyncio.sleep(1)
                    pyautogui.press('enter')
                nhcode = asyncio.create_task(nh.valid_url())
                schleep = asyncio.create_task(asyncio.sleep(delay))
                await schleep

        def txt_mode():
            while True:
                s = choice(txt)
                cpy(s)
                time.sleep(0.69)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                time.sleep(1)
                if flags['r']:
                    pyautogui.press('a')
                    pyautogui.press('backspace')
                    pyautogui.press('up')
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.press('backspace')
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.press('enter')
                time.sleep(delay)

        def copypasta_mode():
            while True:
                cpy(copypasta)
                time.sleep(0.69)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                time.sleep(1)
                if flags['r']:
                    pyautogui.press('a')
                    pyautogui.press('backspace')
                    pyautogui.press('up')
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.press('backspace')
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.press('enter')
                time.sleep(delay)

        if state == TEXT:
            txt_mode()
        elif state == COPYPASTA:
            copypasta_mode()
        elif state == NHENTAI:
            await nh_mode()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
