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

def ini_graph():
    mode("logo")
    speed(0)
    
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
    rectangle(side, side)
    
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
        else:
            my_color = "red"
        
        #draw the position on the screen
        hop(x*side, y*side)
        dot(5, my_color)
        hop(-x*side, -y*side)
    
def main():
    print("Monte-carlo simulation")
    
    ini_graph()
    #rectangle(200,100)
    marg_x = 10
    marg_y = 10
    hop(-window_width()//2 + marg_x, -window_height()//2 + marg_y)
    square_side = min(window_width()-2*marg_x, window_height()-2*marg_y)
    monte_carlo(square_side, 1000)
    
    
    done()
    print("Done!")
    
    
main()

