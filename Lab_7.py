# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:28:42 2019

@author: Fernando
"""

#CS2302
#Fernando De Santiago
#LAB7
#Olac Fuentes, Anindita Nath and Maliheh Zargaran
#last edited 4/32/19 14:28:00 PM
#Section M/W 10:30-11:50
#purpose: To create a maze and display a message if it's possible to be solved. 
#wether the number of walls removed give a correct maze. and to create 3
#algorithms to search and create a path from bottom left corner to upper right.


# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def ELConverter(G):#used to convert adjacency list to edge list
    if G is None:
        return None
    g = []
    for source in range(1,len(G)):
        g.append([G[source-1],G[source]])
    return g

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

def Draw_Solution(Edge,walls2,maze_rows,maze_cols):
    fig, ax = plt.subplots()
    
    # draw edgelist path
    for w in Edge:
        if w[1]-w[0] ==1: #new x
            x0 = (w[0]%maze_cols)+.5
            y0 = (w[0]//maze_cols)+.5
            x1 = (w[1]%maze_cols)+.5
            y1 = (w[1]//maze_cols)+.5
        else:#new y
            x0 = (w[0]%maze_cols)+.5
            y0 = (w[0]//maze_cols)+.5
            x1 = (w[1]%maze_cols)+.5
            y1 = (w[1]//maze_cols)+.5
        ax.plot([x0,x1],[y0,y1],linewidth=3,color='r')
    sx = maze_cols
    sy = maze_rows
    
    #draw inside of the maze
    for w in walls2:
        if w[1]-w[0]==1: #vertical wall
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
        
    #Draw the rim of the maze
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
                
    ax.axis('off') 
    ax.set_aspect(1.0)
    

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


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):#draws the base maze
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
n=NumSets(S)
       

def buildMaze1(m,n,G,duplicate=False):#Creates maze using regular find and union
    count=0
    while count!=m and NumSets(S)>1:
        d = random.randint(0,len(walls)-1)
        C1=walls[d]
        C2=C1[0]
        C3=C1[1]
        if find(S,C2)!=find(S,C3):
            if C2<C3 and C3 not in G[C2]:
                G[C2].append(C3)
                if duplicate:
                    G[C3].append(C2)
            union(S,C2,C3)
            walls.pop(d)
            count+=1
    global walls_2
    walls_2=walls
    return G

def buildMaze2(m,n,G):#creates maze using union_by_size
    count=0
    while count!=m and NumSets(S)>1:
        d = random.randint(0,len(walls)-1)
        C1=walls[d]
        C2=C1[0]
        C3=C1[1]
        if find_c(S,C2)!=find_c(S,C3):
            if C2<C3 and C3 not in G[C2]:
                G[C2].append(C3)
                G[C3].append(C2)
            union_by_size(S,C2,C3)
            walls.pop(d)
            count+=1
    global walls3
    walls3=walls
    return G
 
def breadth_first_search(G,start, end):#used to find shortest path using BFS 
    queue=[(start,[start])]#using queue
    visited=set()#creates an empty set
    while queue:
        (vertex,path)=queue.pop(0)#pop the first number
        if vertex not in visited:#if vertex has not been visited
            if vertex==end:#if vertex is the end then return the path
                return path
            visited.add(vertex)#adds vertex to the set
            for next in G[vertex]:#for any number in G[vertex] then append
                queue.append((next,path+[next]))
            
def depth_first_search_stack(G,S,E):#used to find shortest path using DFS and 
                                    #stacks
   stack = [(S,[S])]#creating stack
   visited=set()    #creates a empty set
   while stack:
       (vertex,path)=stack.pop()#pop the last number
       if vertex not in visited:#if vertex has not been visited
           if vertex==E:#if vertex is equal to the end return the path
               return path
           visited.add(vertex)#adds vertex to the set
           for next in G[vertex]:#for any number in G[vertex] then append
               stack.append((next,path+[next]))

def depth_first_search_recursive(G,S,E,path=[]):#used to find shortest path
                                                #using DFS recursively
    path=path+[S]#adds to the list the path and the vertex S
    checker=True#used to check
    if path[-1]!=E:#if the past item in the path is not the n-1
        for i in G[S]:
            if S==E:#vertex equals the n-1
                checker = False#changes vertex to False
                path2=[]#creates empty path
                path2=path+[S]#does the same as path
                return path2#returns path 2
            if i not in path and checker is not False:
                path= depth_first_search_recursive(G,i,E,path)#recursive call
                if path[-1]==E:#if last item in path is n-1 then return path
                    return path
                else:
                    path.pop(-1)#pop to remove all unneeded items that don't 
                                #lead to the path
    return path

#for i in range(len(walls)//2): #Remove 1/2 of the walls 
#    d = random.randint(0,len(walls)-1)
#    print('removing wall ',walls[d])
#    walls.pop(d)
print('there are',n,'cells')
print('Enter number of walls you wish to remove.')
while True:
    try:
        m = int(input())
        break
    except:
        print("That's not a valid option!")

if m<n-1:
    print("A path from source to destination is not guaranteed to exist.")
elif m==n-1:
    print("There is a unique path from source to destination.")
else:
    print("There is at least one path from source to destination.")


draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

start=time.time()
G = [ [] for i in range(n) ]
buildMaze1(m,n,G,True)
print()
F=(buildMaze1(m,n,G))
print("Starting breadth first search")

start1=time.time()
print(breadth_first_search(F,0,n-1))
end1=time.time()

print("it takes",end1-start1," to create the breadth first search list")
print("converting to edge list")
start3=time.time()
ELB=ELConverter(breadth_first_search(F,0,n-1))
end3=time.time()
print("takes", end3-start3,"to convert")
if ELB is not None:
    start2=time.time()
    Draw_Solution(ELB,walls_2,maze_rows,maze_cols)
    end2=time.time()
    print("it takes",end2-start2," to draw the solution")
print()

print("Starting depth first search using stack")

start4=time.time()
print(depth_first_search_stack(F,0,n-1))
end4=time.time()

print("it takes",end4-start4," to create the depth first search list")
print("converting to edge list")
start5=time.time()
ELDFSS=ELConverter(depth_first_search_stack(F,0,n-1))
end5=time.time()
print("takes",end5-start5,"to convert")
if ELDFSS is not None:
    start6=time.time()
    Draw_Solution(ELDFSS,walls_2,maze_rows,maze_cols)
    end6=time.time()
    print("it takes",end6-start6,"to draw the solution")
print()

print("Starting depth first search using recursion")

start7=time.time()
print(depth_first_search_recursive(F,0,n-1))
end7=time.time()

print("it takes",end7-start7,"to create the depth first search list")
print("converting to edge list")
start8=time.time()
ELDFSR=ELConverter(depth_first_search_recursive(F,0,n-1))
end8=time.time()
print("takes",end8-start8,"to convert")
if ELDFSR is not None:
    start9=time.time()
    Draw_Solution(ELDFSR,walls_2,maze_rows,maze_cols)
    end9=time.time()
    print("it takes",end9-start9,"to draw the solution")
print()
end=time.time()
print("overall time to run all methods using regular union",end-start)
#
#
S=DisjointSetForest(maze_rows*maze_cols)
walls = wall_list(maze_rows,maze_cols)
#
start=time.time()
G = [ [] for i in range(n) ]
buildMaze2(m,n,G)
print()
F=(buildMaze2(m,n,G))
print("Starting breadth first search")

start1=time.time()
print(breadth_first_search(F,0,n-1))
end1=time.time()

print("it takes",end1-start1," to create the breadth first search list")
print("converting to edge list")
start3=time.time()
ELB=ELConverter(breadth_first_search(F,0,n-1))
end3=time.time()
print("takes", end3-start3,"to convert")
if ELB is not None:
    start2=time.time()
    Draw_Solution(ELB,walls3,maze_rows,maze_cols)
    end2=time.time()
    print("it takes",end2-start2," to draw the solution")
print()

print("Starting depth first search using stack")

start4=time.time()
print(depth_first_search_stack(F,0,n-1))
end4=time.time()

print("it takes",end4-start4," to create the depth first search list")
print("converting to edge list")
start5=time.time()
ELDFSS=ELConverter(depth_first_search_stack(F,0,n-1))
end5=time.time()
print("takes",end5-start5,"to convert")
if ELDFSS is not None:
    start6=time.time()
    Draw_Solution(ELDFSS,walls3,maze_rows,maze_cols)
    end6=time.time()
    print("it takes",end6-start6,"to draw the solution")
print()

print("Starting depth first search using recursion")

start7=time.time()
print(depth_first_search_recursive(F,0,n-1))
end7=time.time()

print("it takes",end7-start7,"to create the depth first search list")
print("converting to edge list")
start8=time.time()
ELDFSR=ELConverter(depth_first_search_recursive(F,0,n-1))
end8=time.time()
print("takes",end8-start8,"to convert")
if ELDFSR is not None:
    start9=time.time()
    Draw_Solution(ELDFSR,walls3,maze_rows,maze_cols)
    end9=time.time()
    print("it takes",end9-start9,"to draw the solution")
print()
end=time.time()
print("overall time to run all methods using union by size",end-start)