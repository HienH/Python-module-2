#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:37:45 2018

@author: hienh
"""

####################Task1#######################
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
print (item)

####################Task2#######################

values = [875, 23, 451]
for val in values:
    print('---> '+str(val)) 

for val in values:
    print('---> '+str(val+50))

####################Task3#######################

random = ['this', 'is', 'a', 'random','list']
for word in random:
    print('***', word)
    
####################Task4#######################
hello = "hello"

for char in hello:
    print(char)

####################Task5#######################
tu = (55,'hello','how',4,True)
for item in tu:
    print(item)

####################Task6#######################
dic = {'al':2000, 'bo': 5000, 'ced':1500}

for item in dic:
    print(item, dic[item])

####################Task7#######################

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
print(metals)

metals.sort(reverse=True,key=lambda m:densities[m])
print(metals)

for metal in metals:
    print('{0:>8} = {1:5.1f}'.format(metal,densities[metal]))

####################Task8#######################

for metal in densities:
    if(densities[metal] >= 8):
        print(metal,densities[metal])
        
####################Task9#######################
numbers = [3,4,5,6,7,10]

def sumValues(val):
    total = 0
    for num in val:
        total+= num
    print('total:',total)
    return total

sumValues(numbers)

####################Task10#######################
value = [2,12,8,9]
for i in range(len(values)):
    value[i]= value[i]*2
print(value)

####################Task11#######################
list1 = range(5)
for i in range(len(list1)):
    print(list1[i])
    
for i in list1:
    print(i)
    
list2 = range(2,10)
for i in list2:
    print(i)
list3 = range(2,20,2)
for i in list3:
    print(i)
####################Task12#######################
#break in for loops
nums = [11,2,12,100,203,301,1,200]
for i in range(len(nums)):
    if nums[i] >=100:
        print('found',nums[i],'at index',i)
        break 
    
for i in nums:
    if i >= 100:
        print('found',i)
        break
   
####################Task13#######################

outer_vals = [1, 2, 3]
inner_vals = ['A', 'B', 'C'] 
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)
        
#count variable 
color = ['r','b','g','b','g','r','r','r']
d={}
for i in color:
    if i not in d:
        d[i] =1
    else:
        d[i] += 1
print(d)

out= [1,2,3]
inner=['A','B','C']
dict ={}
for i in out:
    for j in inner:
        print(i,j)
   
        dict[i]=j
print(dict)

####################Task14#######################

for i in range(1,10):
    for j in range(1,11):
        print('{0:>3}'.format(i * j), end='') 
    print('\n')