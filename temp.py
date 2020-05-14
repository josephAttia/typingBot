# -*- coding: utf-8 -*-
from pynput.mouse import Button
from pynput.keyboard import Key
import pynput
import time
import random


mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

for x in range(49):
    time.sleep(2)
    mouse.scroll(0, -3)
    mouse.position = (918, 510)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.scroll(0, 3)
    time.sleep(0.5)
    mouse.position = (741, 556)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)



    def controlKeyboard():
        for char in "Question 2 of the FRQ section will be a prose analysis prompt. You will need to read a given prose passage of 500 to 700 words and a prompt to guide your analytical essay about the passage. The prompt will help you figure out what to look for as you read the passage":
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.01)


    controlKeyboard()
    time.sleep(random.randrange(47, 50))
    keyboard.press('.')
    keyboard.release('.')
    print(x)





