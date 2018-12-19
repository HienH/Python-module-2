#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:24:53 2018

@author: hienh
"""
number = input("Enter a number between 1 and 10 ")
number = int(number)

#Task3

if number >10 :
    print("Too High")
if number< 0 :
    print("Too Low")
    
#Task 4
if  type(number) == int :
    print("you have enter a number")
else:
    print("you have not enter a number")

#Task 5
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