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
        if len(sys.argv) < 3 or len(sys.argv) > 2 and (sys.argv[2] == '1' or sys.argv[2].lower() == 'true'):
            width, height = pyautogui.size()
            # posx, posy = 0.3140625 * width, 0.95 * height
            loc = pyautogui.locateOnScreen('ss.png', grayscale=True)
            posx, posy = pyautogui.center(loc)
            pyautogui.moveTo(posx, posy)
            pyautogui.click()

        chosenOne = s3

        while True:
            s = choice(s3)
            #s = s1
            pyautogui.write(s)
            pyautogui.press('enter')
            time.sleep(62)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
