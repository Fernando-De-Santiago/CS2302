# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:16:50 2019

@author: Fernando
"""
# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019
#CS2302
#Fernando De Santiago
#LAB3
#Olac Fuentes, Anindita Nath and Maliheh Zargaran
#last edited 3/15/19 11:44:00 PM
#Section M/W 10:30-11:50
#purpose: The purpose of this program is to help us learn how to navigate a B-tree
#while also teaching us how to right methods that require us to know how they work.

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
    
#SearchAndPrint(T,60)
#SearchAndPrint(T,200)
#SearchAndPrint(T,25)
#SearchAndPrint(T,20)
#
#print(height(T))
#method 1
def height2(T):
    if T.isLeaf:#if leaf it'll return 0
        return 0
    return 1 + height(T.child[0])#recursively goes down tree and counts
#method 2
def BTreeToSA(T):
   if T.isLeaf: #if it's leaf it returns all items in that node
       return T.item
   Array=[]#creates empty array
   for i in range(len(T.child)):
       Array+=BTreeToSA(T.child[i])#reursively goes down the tree until it reaches the leafs
       if i < len(T.item):#if i is less than the list of items then it
           Array.append(T.item[i])#will append the children nodes and root
   return Array
#method 3
def minimum(T,d):
    if d==0:
        return T.item[0]#if depth is zero return the first item on the left
    elif d<0:#if depth is less than 0 then it shouldn't expect a number
        return 'No items in negative depth'
    elif d>height2(T):#if depth is more than height then an error will occur so added this to stop that
        return 'depth exceded'
    return minimum(T.child[0],d-1)#goes all the way to the left and down the tree depending on the depth
#method 4
def maximum(T,d):
    if d==0:#if depth is 0 return number on the far right of the list
        return T.item[len(T.item)-1]
    elif d<0:#if depth is less than zero than it shouldn't return a number
        return 'No items in negative depth'
    elif d>height2(T):#if depth is more than height then an error will occur so added this to stop it
        return 'depth exceded'
    return maximum(T.child[len(T.item)],d-1)#goes all the way to the right and down depending on the depth
#method 5
def NumItemsD(T,d):
    if d==0:#if depth is 0 then return the length of the leaf
        return len(T.item)
    elif d < 0:#if depth is less than 0 then return -1 as a sign or error
        return -1
    elif T.isLeaf and d>0:#if it's a leaf and depth is greater than zero then an error would occur so return -1
        return -1
    elif d>height2(T):#if depth is more than the height then error would occur so return string
        return 'depth exceded'
    add=0#used to add the number
    for i in range(len(T.child)):
        add+=NumItemsD(T.child[i],d-1)#recursively adds the numbers in the depth requested depth
    return add
#method 6
def printItemsD(T,d):
    if d==0:
        for i in range(len(T.item)):
            print(T.item[i],' ')#if depth is 0 then it'll return the all the items in the node
    elif d>height2(T):
        print('depth exceded')#added error message
    elif d<0:
        print('depth can not be negative')#added error message
    else:
        if T.isLeaf is False:
            for i in range(len(T.child)):
                printItemsD(T.child[i],d-1)#recursively prints items at given depth
            
#method 7
def FullNodes(T):
    counter=0
    if T.isLeaf:#if leaf return 0 
        return counter
    if len(T.item)==T.max_items:#if the length of the items is equal to the max add 1
        counter+=1
    for i in range(len(T.item)):
        counter+=FullNodes(T.child[i])#recursively going through the child and checking if it meets max items
    counter+=FullNodes(T.child[len(T.item)])#goes to the last node and checks it
    return counter
#method 8
def FullLeafs(T):
    sum=0
    if T.isLeaf and len(T.item) == T.max_items:#checks if the leaf is a full node or not
            return 1
    for  i in range(len(T.child)):
        sum+=FullLeafs(T.child[i])#recursively going through to find all the leafs and adding 1 to it
    return sum
#method 9
def FindDepth(T,k): 
    b=0
    while b<len(T.item) and k>T.item[b]:#going in a loop while using a temp counter and adding 1 to it
        b+=1
    if b==len(T.item) or k<T.item[b]:#checks to see if b is either the same as the length of the node or if the key is less than the item in the node at location b
        if T.isLeaf:
            return -1
        else:
            f=FindDepth(T.child[b],k)#recursively adding to f which will return the depth
            if f==-1:
                return -1
            else:
                return f+1
    else:
        return 0
    
print(height2(T))#1 works
print(BTreeToSA(T))#2 works
print(minimum(T,2))#3 works
print(maximum(T,2))#4 works
print(NumItemsD(T,0))#5 works
printItemsD(T,1)#6 works
print(FullNodes(T))#7 works
print(FullLeafs(T))#8 fix
print(FindDepth(T,-100))#9