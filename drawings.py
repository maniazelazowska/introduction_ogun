#this is taken from the lecutre. not related to the following program
#i=1
#L=[1,2,3,4,5]
#i, L[i] = 4, -1
#output will be: 4, [1,2,3,4,-1]
#first we assigned i=4 so we consider L[i] to be L[4]. 
#it is a swap function, so we change L[4]=-1



#program for drawing polygons using turtle
from turtle import *

def drawSquare(size): 
    #a function for drawing a square of given size
    for i in range(4):
        fd(size) #draw a line for {size} units
        lt(90)   #turn left 90 degrees

def drawPolygon(n, size):
    #draws a polygon of a number of n sides of given size
    for i in range(n):
        fd(size)
        lt(360/n)
             
#testing section
def test1():
    for i in range(10, 200, 10): #the second 10: we are progressing from value a (10) up to value b (200) every 10 units
        drawSquare(i)            #basically: range(start, stop, step)

def test2():
    for i in range(20):
        lt(10)
        drawSquare(50)
        
def test3(n, size): #draws n squares with a given size
    for i in range(n):
        lt(360/n) #turn left the 
        drawSquare(size)
        
def test4(n, size): #draws n polygons
    for i in range(n):
        drawPolygon(i+3,size)
    
speed(0) #0 being the highest speed of the turtle
#test1()
#test2()
#test3(20,100)
rt(90)
fd(100)
lt(90)
test4(20,80)

#remember to always turn input to integer, as it is always assumed to be a string
#squareSize = int(input("Enter the size of the square: "))
#drawSquare(squareSize)
done()

#experiments with this one as a homework