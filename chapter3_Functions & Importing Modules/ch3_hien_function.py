#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:37:19 2018

@author: hienh
"""

##task1
#
#print ("What’s your name?")
#name = input()
#
#print ("Hello {}!".format(name))
#
#task 2 
def add(a,b):
    return print(a+b)

add(2,2)
#
#print (range (1,10,2))
#print (range (1,10))
#print (range (10))

#task3

def add_two_numbers_from_args(number1, number2):
 answer = number1 + number2
 print(answer)
 return ("{} plus {} is {}".format(number1, number2, answer))


#Mid-class challenge!
def convert_distance(miles): 
    kilometers = (miles * 8.0) / 5.0
    convertdist = "{} miles to km is {}".format(miles,kilometers)
    print(convertdist)
    return convertdist


#task4
def temperatureconversion(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    converttemp= "temperture from centigrade to fahrenheit is {}, and {} in kevin".format(fahrenheit,kelvin)
    print(converttemp)
    return converttemp

