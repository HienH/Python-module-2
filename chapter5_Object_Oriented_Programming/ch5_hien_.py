#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:09:39 2018

@author: hienh
"""
#################Task1##########################

class Customer(object):
    
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        else:
            self.balance -= amount
            return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
hien = Customer('hien hang', 20000)

##################Task2##########################

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def eat(self):
        print('yum')
#
class Dog(Animal):
    def __init__(self,name,age,breed):
      Animal.__init__(self,name,age)
      self.breed = breed 
    def bark(self):
        print('Woof')
    def trick(self):
        print("dog sits down")




class Cat(Animal):
    def __init__(self,name,age):
      Animal.__init__(self,name,age)
    def Meow(self):
        print('Meow')
    
    def fight(self):
        print("cat uses sratch")
    
        
Lucky = Dog("lucky",2,'poodle')
Mimi= Cat("mimi",2)
Mimi.Meow()
print(Lucky.name)
Lucky.bark()
Lucky.trick()

##################Task3##########################


class Robot():
    def move(self):
        print('...move move move...') 
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
class CookRobot(Robot): 
    def cook(self):
        print ('I make rice')

mrRobot = CookRobot()
mrRobot.cook()

##################Task4##########################

class Dog(Animal): 
    def bark(self):
        print('Woof')
        
class Robot():
    def move(self):
        print('...move move move...') 
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        
class SuperRobot(): 
    def _init_(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
        
    def playGame(self): 
        print('alphago game')
        
    def move(self):
        return self.o1.move()
    
    def bark(self):
        return self.o2.bark()
    
    def clean(self):
        return self.o3.clean()
    

machinepet = SuperRobot()
machinepet.bark()
machinepet.playGame()
machinepet.clean()

