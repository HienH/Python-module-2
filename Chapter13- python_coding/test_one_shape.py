#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:16:31 2018

@author: hienh
"""

from MovingShapes import *
frame = Frame()

shape1 = Square(frame,100)

for i in range (100):
    shape1.moveTick()