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
## debugging using breakpoints 
#1) double click next to the line number of your code to set up a breakpoint,a red circle should
#appear 
#2)you can now run your code in debug mode using debugging buttons on the toolbar
#  - first button is for you to start running your code until the break point.
#  - second button allows you to run your code line-by-line until the breakpoint.
#  - third one is for stepping into the sections (class and functions) 
#  - fourth button is for you to step out when you feel that the error is not related to the current section
#  - fith button is for you to go to the next breakpoint
#  - last, square shaped button is for you to exit debugging mode and go back to normal coding mode.
