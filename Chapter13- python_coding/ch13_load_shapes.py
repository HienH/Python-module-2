#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:22:39 2018

@author: hienh
"""

from Shapes import *

frame = Frame()
s1 = Shape('square',100)
s1.goto(200,100)
x=0 
y=0 
for i in range(100):
   s1.goto(x,y)
   x=x+5
   y=x+5
    
    