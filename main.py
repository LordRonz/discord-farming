def main():
    try:
        import pyautogui
        import time
        from random import choice
        import sys

        with open('./shakespeare.txt') as f:
            s1 = f.read().splitlines()
    
        with open('./potterspells.txt') as f:
            s2 = f.read().splitlines()

        with open('./uzumakibayu.txt') as f:
            s3 = f.read().splitlines()

        time.sleep(3)
        if len(sys.argv) < 2 or (len(sys.argv) > 1 and (sys.argv[1] == '1' or sys.argv[1].lower() == 'true')):
            width, height = pyautogui.size()
            # posx, posy = 0.3140625 * width, 0.95 * height
            loc = pyautogui.locateOnScreen('ss.png', grayscale=True)
            if loc:
                posx, posy = pyautogui.center(loc)
                pyautogui.moveTo(posx, posy)
                pyautogui.click()

        chosenOne = s3

        delay = max(62, 62 if len(sys.argv) < 3 else int(sys.argv[2]))

        while True:
            s = choice(s3)
            pyautogui.write(s)
            pyautogui.press('enter')
            time.sleep(delay)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
