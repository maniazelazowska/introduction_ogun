#verifying the quality of the pseudo random number generator in Python

#the probability of hitting the circle:
"""(assumption: radius = side = 1)
    area of a quarter of the circle/area of the square = 
    ((pi*r^2)/4)*(a^2) = pi/4"""

#structure of program:
    #import(s)
    #functions
    #main function
    #call to main function

from turtle import *
from random import random
from math import pi


def ini_graph():
    mode("logo")
    speed(0)
    tracer(False)   #speeds up the graphics faster and prevents animation
    
#move from current position
def hop(x, y): 
    up()
    fd(y)
    rt(90)
    fd(x)
    lt(90)
    down()
    
    
def rectangle(my_width, height):
    for i in range(2):
        fd(height)
        rt(90)
        fd(my_width)
        rt(90)


def monte_carlo(side, amount):
    #draw a square
    rectangle(side, side)
    
    #draw a quarter of the circle
    color("blue")
    hop(side, 0)      # Required by the circle function starting position of the turtle
    circle(side, 90)
    # Return the turtle to its starting position
    rt(90)
    hop(0, -side)
    
    #init counter
    hits = 0
    
    for i in range(amount):
        #throw a stone to select a place within the square
        x = random()
        y = random()
        
        #decide if the stone hits the circle, 
        #so if (x,y) is less than 1[u] away from (0,0)
        #it's calculated fro sqrt((x-0)^2 + (y-0)^2) = sqrt(x^2+y^2)
        #sqrt(n) < 1 only if n < 1
        if x*x + y*y <= 1:
            my_color = "green"
            hits += 1
        else:
            my_color = "red"
        
        #draw the position on the screen
        hop(x*side, y*side)
        dot(5, my_color)
        hop(-x*side, -y*side)
        
    print(f"Throws: {amount}, hits: {hits}, calculated pi {4*hits/amount:10.8f}, Python's pi {pi:10.8f}")
    
    
def main():
    print("Monte-carlo simulation")
    
    ini_graph()
    #rectangle(200,100)
    marg_x = 10
    marg_y = 10
    hop(-window_width()//2 + marg_x, -window_height()//2 + marg_y)
    square_side = min(window_width()-2*marg_x, window_height()-2*marg_y)
    monte_carlo(square_side, 10) # Do not set values larger than say 100 without tracer(False)
    update()    #to see results
    done()
    print("Done!")
    
    
main()

