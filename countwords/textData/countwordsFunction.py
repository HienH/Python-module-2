#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:03:25 2019

@author: hienh
"""

def Stopwords(para):
    stop_para = open(para, 'r')
    stopwords = []
    for word in stop_para.read().split():
        word = word.strip('\n')
        stopwords.append(word)
    return stopwords

    

def countwords(paragraph,stopword):
    paragraph = open(paragraph, 'r')
    wordcount ={}
    for word in paragraph.read().split():
        if word in stopword:
            continue
        elif word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def countwordsNostop(paragraph):
    paragraph = open(paragraph, 'r')
    wordcount1 ={}
    for word in paragraph.read().split():
        if word not in wordcount1:
            wordcount1[word] = 1
        else:
            wordcount1[word] += 1
    return wordcount1


def printTop20(dict):
    top = sorted(dict.items(),reverse=True, key=lambda t: t[1])
    top20 = top[:20]
    for word in top20:
        print (word)

def similarity(script1,script2,stopword):
    word1 = countwords(script1,stopword)
    word2 = countwords(script2,stopword)

    same = []
    for key1 in word1:
        if key1 in word2:
            same.append(key1)
    
    return round((len(same)/(len(word1)+len(word2)-len(same)))*100,2)

    
    
stopword = Stopwords("stopwords.txt")


