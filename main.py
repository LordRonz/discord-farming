import asyncio

async def main():
    try:
        import pyautogui
        import time
        from random import choice
        import nhentaigen.nhentai_code_generator as nh
        import argparse

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.3

        parser = argparse.ArgumentParser(description='Sucking MEE6\'s cock')
        parser.add_argument('-i', default=3.0, type=float, help='initial delay(sec)', )
        parser.add_argument('-d', default=60.0, type=float, help='delay between messages(sec)')
        parser.add_argument('-l', action='store_true', help='locate textbox')
        parser.add_argument('-r', action='store_true', help='delete message after sending it')
        parser.add_argument('-s', default=None, help='test file source(shakespeare, potter, or uzumaki)')

        flags = vars(parser.parse_args())

        txt = None
        if flags['s'] == 'shakespeare':
            with open('./shakespeare.txt') as f:
                txt = f.read().splitlines()
        
        elif flags['s'] == 'potter':
            with open('./potterspells.txt') as f:
                txt = f.read().splitlines()

        elif flags['s'] == 'uzumaki':
            with open('./uzumakibayu.txt') as f:
                txt = f.read().splitlines()

        # Initial delay
        time.sleep(flags['i'])

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
                pyautogui.write(s)
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
            chosenOne = txt
            while True:
                s = choice(txt)
                pyautogui.write(s)
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
        if txt:
            txt_mode()
        else:
            await nh_mode()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
