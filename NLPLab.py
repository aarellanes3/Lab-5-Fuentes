# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:07:25 2019

@author: aarel
"""

import numpy as np

class BST(object):
    # Constructor
    def __init__(self, item, vector,left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right 

def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
            
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def build_binary(L):
    T = None
    for line in word:
        w = line.split(" ")
        if w.isalpha():
            vector = np.array(50)
            for i in range(1,len(w)):
                vector[i-1] = float(w[i])
            T.Insert(T,[[w[0]][vector]])
    return T

H = HashTableC(11)
A = ['data','structures','computer','science','university','of','texas','at','el','paso']
for a in A:
    InsertC(H,a,len(a))
    print(H.item)

for a in A: # Prints bucket, position in bucket, and word length
    print(a,FindC(H,a))
    
table = input("Do you want to use a hashtable or a binary-search-tree?")

if table == "hashtable": 
    ht = open("glove.6B.50d.txt",'r')
    print("Hello World!")
    
elif table == "binary-search-tree":
    bst = open("glove.6B.50d.txt", encoding ='utf-8')
    word = bst.readlines()
    build_binary(word)
    
else:
    print("not a valid table")    