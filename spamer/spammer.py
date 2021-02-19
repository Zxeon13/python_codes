#!/usr/bin/python
import pyautogui, time

time.sleep(5)
f = open("beemovi.txt",'r')
x=0
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)
    x=x +1
    if (x == 10):
        pyautogui.typewrite("!rank")
        pyautogui.press("enter")
        x=0



            