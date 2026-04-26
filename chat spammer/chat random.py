import random
import pyautogui as pg
import time

me=["hello","how","are","you"]
time.sleep(2)

for a in range(10):
    b=random.choice(me)
    pg.write(b)# it will write to keyboard
    pg.press("enter")
