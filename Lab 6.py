# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:40:03 2019

@author: Fernando
"""

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random


def DisjointSetForest(size):#creates sets * size and fills with -1
    return np.zeros(size,dtype=np.int,order='C')-1

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root

def find_c(S,i):
    #Find with path compression
    if S[i]<0:
        return i
    r= find_c(S,S[i])
    S[i]=r
    return r

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    #uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root

def NumSets(S):#counts all the sets in the set S
    count=0
    for i in range(len(S)):
        if S[i]<0:
            count+=1
    return count

def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j) 
    if ri!=rj: 
        if S[ri]>S[rj]:# j's tree is larger
            S[rj]+=S[ri]
            S[ri]=rj
        else:
            S[ri]+=S[rj]
            S[rj]=ri# Make j's root point to i's root


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 
maze_rows = 10
maze_cols = 15

S=DisjointSetForest(maze_rows*maze_cols)
size=maze_rows*maze_cols
walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
def buildMaze1():#Creates maze using regular find and union
    while NumSets(S)>1:
        d = random.randint(0,len(walls)-1)
        C1=walls[d]
        C2=C1[0]
        C3=C1[1]
        if find(S,C2)!=find(S,C3):
            union(S,C2,C3)
            walls.pop(d)

def buildMaze2():#creates maze using path compresssion
    while NumSets(S)>1:
        d = random.randint(0,len(walls)-1)
        C1=walls[d]
        C2=C1[0]
        C3=C1[1]
        if find_c(S,C2)!=find_c(S,C3):
            union_c(S,C2,C3)
            walls.pop(d)

def buildMaze3():#creates maze using union_by_size
    while NumSets(S)>1:
        d = random.randint(0,len(walls)-1)
        C1=walls[d]
        C2=C1[0]
        C3=C1[1]
        if find_c(S,C2)!=find_c(S,C3):
            union_by_size(S,C2,C3)
            walls.pop(d)

#for i in range(len(walls)//2): #Remove 1/2 of the walls 
#    d = random.randint(0,len(walls)-1)
#    print('removing wall ',walls[d])
#    walls.pop(d)

draw_maze(walls,maze_rows,maze_cols) 

print(NumSets(S))
buildMaze1()
draw_maze(walls,maze_rows,maze_cols) 

maze_rows = 10
maze_cols = 15

S=DisjointSetForest(maze_rows*maze_cols)
size=maze_rows*maze_cols
walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols) 
buildMaze2()

draw_maze(walls,maze_rows,maze_cols) 

S=DisjointSetForest(maze_rows*maze_cols)
size=maze_rows*maze_cols
walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols) 
buildMaze3()
draw_maze(walls,maze_rows,maze_cols) 