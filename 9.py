# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:12:15 2021

@author: tt
"""

import pyautogui as g

test_position= (1424,0)
test_position2= (1500,500)
g.PAUSE =5
g.FAILSAFE = True
print(g.position())
# g.click()
# g.move(100,200)
x= g.locateOnScreen('2.png')
g.moveTo(x)




