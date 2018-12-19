#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:42:59 2018

@author: hienh
"""

from random import randint

def game(attempt,range):
    number = randint(1,range)
    print("Welcome! can you guess my secret number? ")
    print("you have",attempt, "guesses")
    guess = attempt
    result = "playing"
    while guess > 0 :
        answer = int(input("Make a guess: "))
        if answer == number:
            result = "win"
            print("Congratulation you have successfully guessed correctly, You win :} ")
            break
        elif answer < number:
            print("guess again, too low")
            guess = guess - 1 
            print("you have",guess,"guesses left" )
        else:
            print("guess again, too high")
            guess = guess - 1 
            print("you have",guess,"guesses left" )

    if result != "win":
        print("oh no! Your out of guesses, You lose :{ ")
    print("game over")
    
game(4,10)
         
    
    
    