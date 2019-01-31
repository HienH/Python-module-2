#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:19:57 2018

@author: hienh
"""
def DataBundlePurchase(truepin, balance):
    if checkpin(truepin):
        print('\n Please choose your transaction type')
        print('--To check your balance-- Enter 1')
        print('--To top up mobile credit-- Enter 2')
        print('--To exit programme-- Enter 3')

        type =0
        
        while type < 1 or type > 3:

            try:
                type = int(input('Enter 1,2 or 3,\n'))
        
            except ValueError:
                print("invalid choice")
            else:
                if type < 1 or type > 3:
                    print('not in range')
        

        if type == 1:
            print('Your balance is', balance, 'GDP')
            print('Thank you for using this service')
            return ('balance request')
                
        elif type == 2:
            return mobileTopup(balance)
        elif type == 3:
            print('exiting')
            return ("No action")

    
def checkpinOnce(truepin):
    attempt = input('Enter your pin ')
    if attempt == truepin:
        return True
    else:
        print('Incorrect password')
        return False
    
def checkpin(truepin):
    if checkpinOnce(truepin):
        return True
    print('Please try again ,(2nd attempt)')
    if checkpinOnce(truepin):
        return True
    print('Please try again, (final attempt)')
    if checkpinOnce(truepin):
        return True
    return False

def checkmobile():
     if mobilenumber == mobilenumber2 :
        print('You have enter your mobile number correctly')
        credit = int(input('how much would you like to top up'))
        balance = balance + credit
        print ('congrats you have topped up, your new balance is ', balance )
        return balance


def mobileTopup(balance):
    print('You have choosen to top up credit ')
    print('\n Your current balance is ', balance)
    mobilenumber = 000
    mobilenumber2 = 111
    print ('to top up please enter your number twice')
    
    while mobilenumber != mobilenumber2 :
        try:
             mobilenumber = int(input('please enter your mobile number \n'))
             mobilenumber2 = int(input('please enter your mobile number again \n'))
        except ValueError:
                print("not a number")
                print('to top up please enter your number twice')
        else:
            if mobilenumber != mobilenumber2 :
                print('please enter the same numbers')
                print('to top up please enter your number twice')
            
                
             
     
        
    print('\n You have enter your mobile number correctly')
    credit = 1
    while credit %5 != 0:
        try:
            credit = int(input('how  much would you like to top up \nyou can only top-up up multiples of 5: '))
         
        except ValueError:
                print("not a number")
        
        else:
            if credit %5 != 0:
                print('not a multiple of 5, please enter a correct numbers of 5')
             
                           
    if credit > balance:
        return ('Insufficient funds to topup')
    elif (credit % 5 ==0):
       balance = round(balance - credit,2)
       print ('congrats you have topped up, your new balance is ', balance, )
       print ('your new credit is ', credit, )
       return balance

#    else:
#        print('You can only top-up multiples of 5')
#        return('Not a multiples of 5')
#        else:
#            print('Sorry your mobile numbers did not match')
    

    
