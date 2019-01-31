#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:58:32 2019

@author: hienh
"""

from countwordsFunction import *
from itertools import combinations 

#stopword = Stopwords("stopwords.txt")
#print("--------")
#uniqueWordsStop = countwords('mobydick.txt',stopword)
#uniqueWords=countwordsNostop('mobydick.txt')
#
#printTop20(uniqueWordsStop)
#print("--------------------")
#printTop20(uniqueWords)
#
#
#print(similarity('george01.txt','george02.txt',stopword))


###############Task 4: Similarity (optional/challenge)#########################
#print(similarity('george01.txt','george02.txt',stopword))
#print(similarity('george01.txt','george03.txt',stopword))


comb = combinations([1, 2, 3,4], 2)
    
for i in list(comb): 
    print ('compare: (george0'+str(i[0])+'.txt <> george0'+str(i[1])+'.txt) = ', similarity('george0'+str(i[0])+'.txt','george0'+str(i[1])+'.txt',stopword))

