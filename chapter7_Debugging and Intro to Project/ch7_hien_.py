#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:30:14 2018

@author: hienh
"""
###############Task1#############
userInput = input('Please give a number ')
print(type(userInput))
userInput = int(userInput)
result = userInput - 2
print(result)

###############Task2#############

userInput = input('Please give a number ')
def simpleOperation(userInput):
   intInput = int(userInput)
   result = intInput - 2
   return result

def nestedOperation(result):
   result = simpleOperation(userInput)
   result2 = result * 2
   return result2
result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)
