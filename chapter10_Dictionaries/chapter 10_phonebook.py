#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:18:27 2018

@author: hienh
"""
#-function that can generqate phoneBOOK which contains 4 classmates info 
#{Name:[3diget n0.lucky n0, postcode,town/city]}
#- sort dictionary by name 
#sort dictionary by town 
#sory by lucky no.


def phonebook():
    book = {}
    number = phonenum()
    book["num"] = number
    luckynum = luckynumber()
    book["LN"] = luckynum
    post = postcode()
    book["PC"]= post
    town = townlive()
    book["town"]= town
    
    yourage = age()
    book["age"] = yourage
    
    return book["num"],book["LN"],book["PC"],book["town"], book["age"]
    
def phonenum():
    number = input("what is you phone number? ") 
    if len(number)>3:
        lastdigits = number[-1:-4:-1]
        return lastdigits
    else:
        return number
def luckynumber():
    luckynum = int(input("what is your fav number? "))
    return luckynum
def postcode():
    post = input("what is your postcode? ")
    return post
def townlive():
    town = input("what is your town? ")
    return town
def age():
    age = input("what is your age? ")
    return age


def diffage():
    ownage= int(input("What is your age? "))
    age = 92- ownage
    return age 

#name1= input("what is your name? ")
#person1 = phonebook()
#name2= input("what is your name? ")
#person2 = phonebook()
##name3= input("what is your name? ")
##person3= phonebook()
#
#phoneNumber = {}
#phoneNumber[name1]= person1
#phoneNumber[name2]=person2
##phoneNumber[name3]=person3
#print(phoneNumber)

#def sortPhone(a):
#    if (a == 'name'):
#        sortphonebook= sorted(phoneNumber.items(), key=lambda kv: kv[0])
#        return sortphonebook
#    elif (a == 'town'): 
#        sortphonebook= sorted(phoneNumber.items(), key=lambda kv: kv[1][4])
#        return sortphonebook
#    elif (a == 'lucknumber'):
#        sortphonebook= sorted(phoneNumber.items(), key=lambda kv: kv[1][1])
#        return sortphonebook
#
#a = input("how would you want your phone book to be sorted; enter 'name','town' or 'luckynumber'? ")
#sortedPhoneBook= sortPhone(a)
#print(sortedPhoneBook)

##challenge 2 
    
def add_classmate_info(phoneBook_dict):
   while True:
       nextClassmate = input ('Would you like to enter another student? Y/N ')
       if nextClassmate == 'N':
           break
       name = input('What is your name? ')
       phoneNo = input('What are the last 3 digits of your phone number? ')
       luckyNo = input('What is your lucky number? ')
       postCode = input('What is your postcode? ')
       townOrCity = input('what is your home town or city? ')
       age = int(input('What is your age? '))
       phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity, age
       print(str('The queen has had ') + str(queenAge - age) + str(' more years on earth than you.'))
       print(phoneBook_dict)
     

