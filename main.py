import pyautogui
import time
from random import choice

pyautogui.moveTo(603, 1014)
pyautogui.click()
s1 = '''
In William Shakespeare's Hamlet, "to be, or not to be, that is the question." In the 21st century, "to code, or not to code, that is the challenge.
All that glitters is not gold
By the pricking of my thumbs, Something wicked this way comes. Open, locks, Whoever knocks!
Now is the winter of our discontent.
Good night, good night! parting is such sweet sorrow, That I shall say good night till it be morrow.
Hell is empty and all the devils are here.
A horse! a horse! my kingdom for a horse!
The lady doth protest too much, methinks.
These violent delights have violent ends...
Brevity is the soul of wit.
'''
s2 = [
    'EXPECTO PATRONUM',
    'AVADA KEDAVRA',
    'WINGARDIUM LEVIOSA',
    'EXPELLIARMUS',
    'SECTUMSEMPRA',
    'EXPECTO PATRONUM',
        ]
for i in range(1000):
    s = choice(s2)
    #s = s1
    pyautogui.write(s)
    pyautogui.press('enter')
    time.sleep(62)
