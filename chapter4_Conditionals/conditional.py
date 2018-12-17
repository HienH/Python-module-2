#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:24:53 2018

@author: hienh
"""

#number = input("Enter a number between 1 and 10 ")
#number = int(number)
#
#if number >10 :
#    print("Too High")
#
#
#elif number< 0 :
#    print("Too Low")
#    
#    
#Task 2

age = input("Enter your age ")
age = int(age)

if  age < 13:
    print('child')
elif age < 18 :
    print('teen')
    
elif age < 65 :
    print('adult')
else:
    print ('pensioner')