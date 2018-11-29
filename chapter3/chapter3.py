#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:20 2018

@author: hienh
"""

"""
name = input('What is your name?').upper()
print('Hello {}!'.format(name))

age = input('What is your age?')
print('hello {} You are {} years old'.format(name,age))
"""
def add(a,b):
    added = int(a)+int(b) 
    print("Your lucky number generator is: " +str(added))
        

def hello():
    name = input('What is your name?')
    a = input('What is your fav number?')
    b = input('What is your age?')

    print('Hello {}!'.format(name))
   
    add(a,b)
    
hello()

