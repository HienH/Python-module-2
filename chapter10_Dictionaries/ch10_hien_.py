#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:56:19 2018

@author: hienh
"""
#####################Task1###########################
salary = {}
salary['al'] = 20000
salary['bo'] = 50000
salary[7] = ('Joke', 'Chen', 'Bond')
print(salary)
print(salary['bo'])
#####################Task2###########################
overwrite dictionary 
salary['bo'] = 55000
salary['al'] += 2000
print(salary)
own dictionary 

#####################Task3###########################

numbers = {}
numbers['hien'] = 9897
numbers['katie']= 7876
numbers['harriet'] = 8897
numbers['police'] = 9991


#update value/lookup/del
print(numbers['hien'])
numbers['hien']= 7942
del numbers['hien']
print(numbers)


#####################Task4###########################

print(numbers.keys())
print(numbers.values())

#####################Task5###########################

print(list(numbers.keys()))
print(list(numbers.values()))

#####################Task6###########################

k = input('search for name ')
if k in numbers:
   print(k, ':', numbers[k])
else:
   print(k, 'not found!')

#####################Task7 & 8###########################
#Sorting a dictionary 
labels = list(numbers.keys())

labels.sort(key=lambda v:numbers[v])
print(labels)
#sort via key and value decending 
keys= sorted(numbers.items(), key=lambda kv: kv[1],reverse=True)
print(keys)

#excerise 1
luckyNumbers = {'katie':[7,4,3], 'harriet':[7,6,10], 'ottilie':[3,9,11], 'hien':[1,2,1]}
##sort the dictionary's in accending order
label_numbers = list(luckyNumbers.keys())
label_numbers.sort(key=lambda v:luckyNumbers[v])
print(label_numbers)

keys = sorted(luckyNumbers,key=lambda k:luckyNumbers[k])
#sort on second value 
keys= sorted(luckyNumbers.items(), key=lambda kv: kv[1][2],)

print(keys)

exercise 2 
random = {'kate': [1,2,90,6], 'harriet':[20,29,1,11],'hien':[10,11,12,13]}
print(random)
keys= sorted(random.items(), key=lambda kv: kv[1][2])
print(keys)
