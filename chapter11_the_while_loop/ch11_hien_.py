#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:07:14 2018

@author: hienh
"""

###################Task1#######################
#repeated division 
x = 40
while x>= 1:
    print(x,':',end='')
    x=x/2
    
###################Task2#######################
#triangular numbers
def tirangular():
    n = int(input("choose a number? "))
    result = 0 
    while n > 0:
        result = result + n
        n = n-1 
    return result

print(tirangular())


###################Task3#######################
#student's Mark

n = int(input("what if your mark"))
while n> 0 :
    if n >=70 :
        print("Congratulation! , first class")
        break
    elif n>= 40:
        print("well done, you passed")
        break
    else:
        print("oh no, you failed ")
        break

###################Task4#######################
def hello():
    name = ""
    print(type(name))
    while type(name) == str:
        name = input("what is your name? ")
        if name == "done":
            break
        else:
            print("hello "+ name)

hello()

###################Task5#######################
#guessing game

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


###################Task6#######################


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