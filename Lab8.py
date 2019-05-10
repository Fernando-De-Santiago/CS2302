# -*- coding: utf-8 -
#CS2302
#Fernando De Santiago
#LAB7
#Olac Fuentes, Anindita Nath and Maliheh Zargaran
#last edited 5/9/19 19:29:00 PM
#Section M/W 10:30-11:50

#purpose of lab is to get a hand of randomized algorithms and backtracking.
"""
Created on Thu May  9 09:44:26 2019

@author: Fernando
"""

import random
import numpy as np
import mpmath

def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        t = random.uniform(-mpmath.pi,mpmath.pi)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True


def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]


def partition(S,S2):
    if sum(S)%2!=0:#if summation of sum is odd then return error message
        return "No partition exists"
    else:
        res,s,=subsetsum(S,len(S)-1,sum(S)//2)#gets one set
        if len(s)==0:#checks if length of set is 0 if it is return error message
            return "No partition exists"
        for i in s:#checks every number in set s
            counter=0#used to get position
            for j in S:#checks all numbers in big set S
                if i == j:#if i and j are the same then pop it out of big S
                    S.pop(counter)
                counter+=1
        return s,S

            
def discover(S):
    for i in range(len(S)):#goes through all the strings
        for j in range(i,len(S)):#goes through all the string starting at i
            if(equal(S[i],S[j])):#uses equal method to check if similar
                print(S[i],S[j]) 
                
    
S=['mpmath.sin(t)','mpmath.cos(t)','mpmath.tan(t)','mpmath.sec(t)','-mpmath.sin(t)','-mpmath.cos(t)','-mpmath.tan(t)',
     'mpmath.sin(-t)','mpmath.cos(-t)','mpmath.tan(-t)','mpmath.sin(t)/mpmath.cos(t)','2*mpmath.sin(t/2)*mpmath.cos(t/2)',
     'mpmath.sin(t)**2','1-mpmath.cos(t)**2','(1-mpmath.cos(2*t))/2','1/mpmath.cos(t)']
#
Set2=[2,4,5,9,12]
discover(S)
print(partition(Set2,Set2))