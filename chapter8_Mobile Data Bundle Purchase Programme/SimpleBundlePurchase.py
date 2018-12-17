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
        
        type = input('Enter 1 or 2,\n')
        
        if (type == '1'):
            print('Your balance is', balance, 'GDP')
            print('Thank you for using this service')
            return ('balance request')
        elif (type == '2'):
            return mobileTopup(balance)
        else:
            print('Error transaction not recognized')
            return ('transaction error')
        
    else:
        print('Authorisation failed, too many attempt of incorrect pin, try again in 5mins ')
        return "Pin error"
   
    
    
    
    
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
    mobilenumber = input('To top up, please enter your mobile number \n')
    mobilenumber2 = input('please enter your mobile number again \n')
    if mobilenumber == mobilenumber2 :
        print('\n You have enter your mobile number correctly')
        credit = int(input('how  much would you like to top up \nyou can only top-up up multiples of 5: '))
        if credit > balance:
            return ('Insufficient funds to topup')
        elif (credit % 5 ==0):
           balance = balance - credit
           print ('congrats you have topped up, your new balance is ', balance )
           return balance

        else:
            print('You can only top-up multiples of 5')
            return('Not a multiples of 5')
    else:
        print('Sorry your mobile numbers did not match')
        
    
    
