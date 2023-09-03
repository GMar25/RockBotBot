from pyautogui import *
from AppOpener import open, close
import time

open("BlueStacks X")
time.sleep(15)

moveTo(750,150)
click()
for elem in "rockbot":
    press(elem)

moveTo(1050,200)
click()

time.sleep(1)

moveTo(1000,500)
click()
moveTo(1200,725)
click()


while False:
    if locateOnScreen('checkin.JPG',confidence=.95):
        print("SLAY")
    elif locateOnScreen('HQ.JPG',confidence=.95):
        print("?")
    else:
        time.sleep(3)
        print('lol')

time.sleep(1)


while False:
    time.sleep(3)
    if locateOnScreen('profile.jpg',confidence=0.9):
        print('Present')
    else:
        print("no good")