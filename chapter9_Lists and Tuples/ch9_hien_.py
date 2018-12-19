#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:40:42 2018

@author: hienh
"""
############Task1########################
x = ['hello', 'this','is','my','first','list']
print(x[0])

############Task2########################
#Modify the list
x = ['this', 55, 'that', 'my_favourite_fruits']
x.remove('my_favourite_fruits')
print(x)
x[1] = 'and'
print(x)
x.append('again')
print(x)

############Task3########################

#list operation 
x = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = x + y

print(z)
print((x + y))

#slice of list
x = ['this', 'and', 'that', 'once', 'again']
x = (x[1:4])
print(x)
##############Task4########################

sort a list
y = [7,11,3,9,2]
y = sorted(y)
print(y)

x =[7, 11, 3, 9, 2]
x.sort()
print(x)

sort() mutates the list sorted() return new object 

 reverse sort
z = sorted(x,reverse=True)
print(z)
##############Task5########################

#Tuples
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
del a[-1]
print(a) ##cannot item in Tuple
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b[0] = 50
print(b) ## cannot assign new value
b.append('z') ## cannot append existing tuple
 
##############Task6########################

# Lambda
x =[4, 14, 3, 9, 2]
y = [7,19,3,9,2]
z = [1, 5, 'sat','on', 'the', 'mat']

x2 = [('a', 3, z), ('c', 8, y), ('b', 5, x)]
x2 = sorted(x2)
print(x2)
# sort by the second value instead: second item of the tuple
x2 = sorted(x2, key=lambda s:s[2][1]) #sort out based on the second tuple, 1st index
print(x2)

##exercise 06
h = [3,5,80,'hello']
i = [5,7,10,'two']
e = [1,3,7,9]
x3 = [(1,'a',6, h),(30,'g',10,i), (20,'j',8,e)]
x3 = sorted(x3)
print(x3)
x3 = sorted(x3, reverse = True)
print(x3)
x3 = sorted(x3, key=lambda s:s[1]) #sort out based on the second value
print(x3)

 