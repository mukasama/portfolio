# Section 009
# 09/17/2012
# Project 02

import turtle
import time
import random

print("This program draws squares of many colors.")
print("------------------------------------------")

print()

# Code bellow prompts the user to enter a whole number.
num_str = input("Enter the number of squares to draw: ")

# num_str checks to see if there is a number in the string, where the user
# is prompted to enter the number of squares to draw.

if num_str.isdigit():
        num_int = int(num_str)

# Gives the user the error messege bellow when they don't enter a whole number.        
while not num_str.isdigit():
        print("The number you entered is not a digit, enter a digit")
        num_str = input("Enter the number of squares to draw: ")

num_int = int(num_str)

# Rotates turtle to the left 360 degrees, then divides it by the number squares
# the user has entered to draw.
turtle.left(360/num_int)
for i in range(num_int):

        # This command sets the pen state to be down and start drawing.
        turtle.down()

        # Used before drawing the shape, so that it will begin to fill in the shape. 
        turtle.begin_fill()

        # Prompts turtle to draw a shape with 4 sides (square).
        for g in range (4):

                # Makes turtle to draw shapes using random colors it chooses.
                turtle.color(random.random(),random.random(), random.random())

                # Moves turtle forward based on the distance that is indicated in the
                # case it will move it forward by 100.
                turtle.forward(100)
                # Turns the turtle to the right 90 degrees of what its drawing.
                turtle.right(90)
        
        # After the shape(s) has been drawn, then this command will end the color
        # fill in all the shapes.
        turtle.end_fill()

        # This command sets the pen state to be up and stops drawing. 
        turtle.up()
        
        turtle.left(360/num_int)

# Lets the turtle window to be open for 5 seconds.
time.sleep(5)

# Prompts turtle to close.
turtle.bye
