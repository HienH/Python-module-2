#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:37:19 2018

@author: hienh
"""
"""
#task1

print ("What’s your name?")
name = input()

print ("Hello {}!".format(name))

#task 2 
def add(a,b):
    return print(a+b)
add(2,2)

print (range (1,10,2))
print (range (1,10))
print (range (10))

#task3

def add_two_numbers_from_args(number1, number2):
 answer = number1 + number2
 print ("{} plus {} is {}".format(number1, number2, answer))

add_two_numbers_from_args(6,8)
"""
#Mid-class challenge!
def convert_distance(miles): 
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:") 
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)


convert_distance(122.5)

#task4
def temperatureconversion(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    print("Converging centigrate to fahrenheit and kelvin")
    print("Centigrafe to kelvin:",kelvin)
    print("Centigrafe to fahrenheit:",fahrenheit)

temperatureconversion(50)