from turtle import *

def initialize_graphics():
    #Initializes turtle graphics.
    mode("logo")
    
def draw_rectangle(rectangle_width, rectangle_height, rectangle_color):
    """
    Draws a rectangle with given parameters 
    starting with its lower-left corner at turtle's positon.
    """
    color(rectangle_color, rectangle_color)
    begin_fill()
    for i in range(2):
        fd(rectangle_height)
        rt(90)
        fd(rectangle_width)
        rt(90)
    end_fill()
    
def hop(x,y):
    """
    Moves the turtle
    """
    up()
    fd(y)
    rt(90)
    fd(x)
    lt(90)
    down()
    
def draw_house(house_width, house_height, house_color, windows_amount, floors_amount):
    """
    Draws a house starting with its lower-left corner at turtle's positon.
    """
    floor_height = house_height//(floors_amount+1)
    
    #draws main part of the building
    draw_rectangle(house_width, floors_amount * floor_height, house_color)
    
    #draw roof
    hop(0,floors_amount*floor_height)
    draw_rectangle(house_width, floor_height, "black")
    
    #return turtle to the starting position
    hop(0, -floors_amount*floor_height)
    
def main():
    print("Start!")
    initialize_graphics()
    hop(0, -200)
    draw_house(100, 50, "green", 3, 4)
    done()
    print("Finished!")
    
    
main()
    