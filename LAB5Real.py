# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:47:34 2019

@author: Fernando
"""
# Code to implement a HashTable and BST
# Programmed by Olac Fuentes
# Last modified April 4th, 2019
#CS2302
#Fernando De Santiago
#LAB5
#Olac Fuentes, Anindita Nath and Maliheh Zargaran
#last edited 3/15/19 21:48:00 PM
#Section M/W 10:30-11:50
#purpose: to read files with python and import and test values with hash and BST
import time
import numpy as np
from numpy import array
from statistics import stdev 
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right  

def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif (T.item[0]) >(newItem[0]):
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or str(T.item[0]) == str(k):#comparing strings
        return T
    if str(T.item[0])<str(k):
        return Find(T.right,k)
    return Find(T.left,k)

def Numbers(T):#counting nodes
    if T is None:
        return 0
    if T is not None:
        Counter=1+Numbers(T.left)+Numbers(T.right)
        return Counter
    
def height(T):#gets height
    if T is None:
        return 0
    left=1
    right=1
    left+=height(T.left)
    right+=height(T.right)
    if left>right:
        return 1+left
    return 1+right

        
def BSTTree():#creates BST
     try:
        with open("glove.6B.50d.txt",encoding='utf-8') as f:
            liners=f.readline()
            T=None
            while liners:
                EA=[]#empty array
                EA=liners.split(" ")
                if EA[0].isalpha():
                    N=((EA[1:]))
                    T=Insert(T,(EA[0],N))
                liners=f.readline()
            return T
     except:
       print("File not found")

       
def contrast(T):#used to find similiarties
     try:
        with open("pairs.txt",encoding='utf-8') as f:
            liners=f.readline()
            counter=0
            while liners:
                EA=[]
                EA=liners.split(" ")
                Word0= Find(T, EA[0])
                print(EA[0],EA[1])
                Word1= Find(T,EA[1])
                print(Word0)
                print(Word1)
                counter+=1
                dot = np.sum(Word0*Word1,dtype=float)#tried using the num.sum method
                print(dot)#tried getting the dot product
                liners=f.readline()
     except:
       print("File not found")
#---------------------------------------------------------------------------------        
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
    for c in str(s):#changed to string
        r = (r*len(str(s)) + ord(c))%n#getting string and get the ord
    return r

def BuildH():#Creating the Hash Table
    try:
        with open("glove.6B.50d.txt",encoding='utf-8') as f:
            lines=f.readline()
            words=[]
            E=[]
            while lines:
                A=[]
                A=lines.split(" ")
                if A[0].isalpha():
                    words.append(A[0])
                    E.append((A[1:]))
                    InsertC(H,words[0],E)
                lines=f.readline()
            return H
    except:
       print("File not found")

def STD(H):#trying to get the Standard Deviation
    try:
        with open("Pairs.txt",encoding='utf-8') as f:
            lines=f.readline()
            E=[]
            while lines:
                lists=lines.split(" ")
                if lists[0].isalpha():
                    E.append((lists[1:]))
                lines=f.readline()
            a=array(E)
            return a
        
    except:
       print("File not found")
def LoadFactor(H):#creating load factor
    if H is None:
        return -1
    counter=0
    for i in range(len(H.item)):
        counter+=len(H.item[i])
    sums= counter/len(H.item)
    return sums

def Double(H):#doubles size
        HT=HashTableC(2*len(H.item)+1)
        for i in range(len(H.item)):
            for j in range(len(H.item[i])):
                InsertC(HT,((H.item[i])[j])[0], ((H.item[i])[j])[1])
        return HT 

def Percent(H):
    empty=0
    for i in H.item:
        if len(i)==0:
            empty+=1
    empty=empty/2    
    return (empty/len(H.item))*100

#------------------------------------------------------------------------------
print("please choose a table implementation")
print("1. Binary Search Tree")
print("2. Hash Table with Chaining")
choice=int(input('decision '))
if choice==1:
    print()
    print("Building Binary Search Tree")
    T=BSTTree()
    print()
    print("Binary Search Tree stats: ")
    print("number of nodes: ")
    print(Numbers(T)+1)
    print("Height: ")
    print(height(T))
    print("Running time for binary search tree construction")
    start=time.time()
    BSTTree()
    end=time.time()
    print(end-start, ' seconds')
    print("Reading word file to determine similarities")
    
    contrast(T)
    print()
    print("running time for binary search tree query processing: ")

elif choice==2:
    H=HashTableC(97)
    H=BuildH()
    print("Building hash table with chaining")
    print()
    print("Hash table stats")
    print()
    print("Initial table size: ",len(H.item))
    while LoadFactor(H)>=1:
         H=Double(H)    
    print("Final table size: ",len(H.item))
    
    print("Load factor: ",LoadFactor(H))
    
    print("Percentage of empty lists: ",Percent(H))

    print("Standard deviation of the lengths of the lists: "%(stdev(STD(H))))

    print()
    print("Reading word file to determine similarities")
    print()
    print("Word similarities found: ")
    print()
    print("Running time for hash table query processing: ")
else:
    print("invalid")
    