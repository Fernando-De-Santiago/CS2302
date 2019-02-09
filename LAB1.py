#CS2302, Fernando De Santiago, LAB1, Olac Fuentes, Anindita Nath and Maliheh Zargaran, last edited 1/27/19 8:58:12 PM, Section M/W 10:30-11:50
"""
Created on Mon Feb  4 08:17:26 2019
@author: Fernando
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def draw_squares(ax,n,perimeter,percent):
    if n>0:
        area = perimeter*percent
        perimeter2=np.copy(perimeter)#creating a copy of the array perimeters
        perimeter2[:,1]+=1000#adding 1000 to the y column to move it up
        perimeter3=np.copy(perimeter)#creating another copy of the array perimet`ers
        perimeter3[:,0]+=1000#adding 1000 to move it to the right
        area2= perimeter2*percent#getting the area for the new squares in the corners
        area3=perimeter3*percent#getting area for the new squares in the corners
        ax.plot(perimeter[:,0],perimeter[:,1],color='k')
        draw_squares(ax,n-1,area+500,percent)#upper right corner
        draw_squares(ax,n-1,area2,percent)#upper left corner
        draw_squares(ax,n-1,area,percent)#bottom left corner
        draw_squares(ax,n-1,area3,percent)#bottom right corner
        
plt.close("all") 
orig_size = 1000
perimeter = np.array([[250,250],[250,750],[750,750],[750,250],[250,250]])
fig, ax = plt.subplots()
draw_squares(ax,2,perimeter,.50)
ax.set_aspect(1.0)
plt.show()
fig.savefig('squares.png')
fig,ax1=plt.subplots()
draw_squares(ax1,3,perimeter,.5)
ax1.set_aspect(1.0)
plt.show()
fig.savefig('squares1.png')
fig,ax2=plt.subplots()
draw_squares(ax2,4,perimeter,.5)
ax2.set_aspect(1.0)
plt.show()
fig.savefig('squares2.png')
#Square ends here
#circle Starts here
def circle(center,rad):
    n = int(4*rad*math.pi)#radius of each circle
    t = np.linspace(0,6.3,n)#creating the circles
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot((x+radius),y,color=(0,0,0))#shifts origin to the left
        draw_circles(ax,n-1,center,radius*w,w)
       
fig, ax3 = plt.subplots() 
draw_circles(ax3, 10, [100,0], 50,.5)
ax3.set_aspect(1.0)
plt.show()
fig.savefig('circles.png')
fig, ax4 = plt.subplots() 
draw_circles(ax4, 20, [100,0], 50,.7)
ax4.set_aspect(1.0)
plt.show()
fig.savefig('circles2.png')
fig, ax5 = plt.subplots() 
draw_circles(ax5, 50, [100,0], 50,.9)
ax5.set_aspect(1.0)
plt.show()
fig.savefig('circles3.png')


#circle ends here
#binary tree starts here
def draw_line(ax, x1,y1,x2,y2):
  n = max( abs(x1-x2), abs(y1-y2) )#the range of the lines
  x = np.linspace(x1,x2,n)
  y = np.linspace(y1,y2,n)
  ax.plot(x,y,color='k')

def recur_graph(ax, x, y, width, height, tiers):
	if tiers > 0:
		draw_line(ax, x+width/2,y, x+width/4,y+height)#drawing line to the left down
		draw_line(ax, x+width/2,y, x+width*3/4,y+height)#drawing line to the right down
		
		tiers -= 1
		recur_graph(ax, x, y+height, width/2, height, tiers) #moving the tree down slowly
		recur_graph(ax, x+width/2, y+height, width/2, height, tiers)#mocing the tree in different directions slowly

def graph(ax, x, y, width, height, tiers):
	tier_height = height/tiers #how much each tier goes down
	recur_graph(ax, x, y, width, tier_height, tiers)
	
fig, ax6=plt.subplots()
graph(plt,0,0,100,-100,3) #plot starting at [0,0] and going to [100,-100] and doing it 3 times each time getting smaller in tier but lower down
ax6.set_aspect(1.0)
plt.show()
fig.savefig('tree.png')
fig, ax7=plt.subplots()
graph(plt,0,0,100,-100,4)#plot starting at [0,0] and going to [100,-100] and doing it 4 times each time getting smaller in tier but lower down
ax7.set_aspect(1.0)
plt.show()
fig.savefig('tree2.png')
fig, ax8=plt.subplots()
graph(plt,0,0,100,-100,5)#plot starting at [0,0] and going to [100,-100] and doing it 5 times each time getting smaller in tier but lower down
ax8.set_aspect(1.0)
plt.show()
fig.savefig('tree3.png')

#tree ends here
#cirlces number 2 starts here
def circle2(center,rad):
    n = int(4*rad*math.pi)#the radius of each circle
    t = np.linspace(0,6.3,n)#creating the circle
    x = center[0]+rad*np.sin(t)#x radius
    y = center[1]+rad*np.cos(t)#y radius
    return x,y

def draw_circles2(ax,n,center,radius):
    if n>0:
        x,y = circle2([center[0],center[1]],radius)# the origin points
        ax.plot(x,y,color='k')
        newrad=radius/3#radius needed to make the circles smaller
        offset=newrad*2#radius used to move the circles up,down,left or right
        draw_circles2(ax,n-1,[center[0],center[1]],newrad)#center circle
        draw_circles2(ax,n-1,[center[0]-offset,center[1]],newrad)#moving the circle right
        draw_circles2(ax,n-1,[center[0]+offset,center[1]],newrad)#movinf the cirlce left
        draw_circles2(ax,n-1,[center[0],center[1]-offset],newrad)#moving the circle up
        draw_circles2(ax,n-1,[center[0],center[1]+offset],newrad)#moving circle down
fig, ax9 = plt.subplots() 
draw_circles2(ax9, 3, [0,0], 30)
ax9.set_aspect(1.0)
plt.show()
fig.savefig('circles4.png')
fig, ax10 = plt.subplots() 
draw_circles2(ax10, 4, [0,0], 30)
ax10.set_aspect(1.0)
plt.show()
fig.savefig('circles5.png')
fig, ax11 = plt.subplots() 
draw_circles2(ax11, 5, [0,0], 30)
ax11.set_aspect(1.0)
plt.show()
fig.savefig('circles6.png')

