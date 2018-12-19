#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:52:25 2018

@author: hienh
"""
from random import randint

def diceGame():

    print("Guess whether the random number is odd or even")
    rounds = int(input("how many rounds do you want to play? "))
    result = "playing"
    while rounds> 0:
        number1 = randint(1,6)
        number2 = randint(1,6)
        number = number1 + number2

        print(number1)
        print(number2)
        answer = input("is the number odd or even? ")
        if number % 2 == 0 and answer == "even":
            result = "win"
            print(result)
            print("Congratulation you have successfully guessed correctly, You win :} ")
            break;
        elif number % 2 == 1 and answer == "odd":
            result = "win"
            print("Congratulation you have successfully guessed correctly, You win :} ")
            break;
        else:
            print("wrong guess, try again. You have", rounds, "left")
            rounds = rounds - 1
            
    if result != "win":
        print("oh no! Your out of guesses, You lose :{ ")
    
    print("game over")
            
diceGame()