# -*- coding: utf-8 -*-
from pynput.mouse import Button, Controller
import time
"""
Created on Wed May 13 16:32:03 2020

@author: 1595187
"""
mouse = Controller()
time.sleep(2)
print ("Current position: " + str(mouse.position))