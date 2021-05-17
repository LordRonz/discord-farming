def main():
    import pyautogui
    from time import sleep

    pyautogui.PAUSE = 0.69

    sleep(3)

    while True:
        pyautogui.write('pls beg', interval=0.1)
        pyautogui.press('enter')
        sleep(45)

if __name__ == '__main__':
    main()