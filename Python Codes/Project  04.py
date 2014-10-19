# Section 09
# 10/ 08/ 2012
# Project 04

import turtle

turtle.goto(100,0)

# Function draw_rectangle, draws a rectangle with desginated lenght and height which then fills in the color(s).
def draw_rectangle(length,height,color):

    turtle.pendown()
    turtle.color(get_color(color))
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.penup()

# Function draw_rectangle2 draws the outline of the rectangle with same lenght along with the desginated lenght, height and color.
def draw_rectangle2(length,height,color):

    turtle.pendown()
    turtle.color(get_color(color))
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.penup()

# The get_color function is used to determine red, blue and white colors from a parameter color sting.
def get_color(color):
    if color == "red":
        return 1,0,0
    if color == "blue":
        return 0,0,1
    if color == "white":
        return 1,1,1
    if color == "black":
        return 0,0,0

# Draw_star function draws a star with desginated angles and lengths which then fills it with the color.
def draw_star(size, color):

    turtle.pendown()
    turtle.begin_fill()
    turtle.color(1,1,1)
    turtle.forward(2.5) 
    turtle.left(size)
    turtle.forward(2.5)
    turtle.right(144)
    turtle.forward(2.5)
    turtle.left(size)
    turtle.forward(2.5)
    turtle.right(144)
    turtle.forward(2.5)
    turtle.left(size)
    turtle.forward(2.5)
    turtle.right(144)
    turtle.forward(2.5)
    turtle.left(size)
    turtle.forward(2.5)
    turtle.right(144)
    turtle.forward(2.5)
    turtle.left(size)
    turtle.forward(2.5)
    turtle.right(144)
    turtle.end_fill()
    turtle.penup()

# draw_flag is a function that draws a fag of a certain heing.    
def draw_flag(height):

    size = 72
    color = "white"

# Letters "a" is just a variable I choose to complete my formula to draw the small blue rectangle.
    
    for a  in range(7):

        turtle.speed(100)
        turtle.down()
        draw_rectangle(height/13,height*1.9,"red")
        turtle.right(90)
        turtle.forward((height/13)*2)
        turtle.left(90)
            
    draw_rectangle(height, height*1.9, "white")

    turtle.goto(100,0)
    draw_rectangle2(height,324,"black")
    
    turtle.goto(-93.5, 0)
    draw_rectangle(height*.5385,height*.76, "blue")

# Letters b, c, d, e, f, g, h, i, j, k are just variables I choose to complete my formula to draw the 50 stars.
   
    turtle.goto(-218,-6)
    for c in range(6):
        draw_star(size, 'white')
        turtle.forward(22)

    turtle.goto(-209,-16)
    for d in range(5):
        draw_star(size, 'white')
        turtle.forward(23) 

    turtle.goto(-218,-26)
    for e in range(6):
        draw_star(size, 'white')
        turtle.forward(22)

    turtle.goto(-209,-36)
    for f in range(5):
        draw_star(size, 'white')
        turtle.forward(23)
        
    turtle.goto(-218,-46)
    for g in range(6):
        draw_star(size, 'white')
        turtle.forward(22)
        
    turtle.goto(-209,-56)
    for h in range(5):
        draw_star(size, 'white')
        turtle.forward(23)

    turtle.goto(-218,-66)
    for i in range(6):
        draw_star(size, 'white')
        turtle.forward(22)

    turtle.goto(-209,-76)
    for j in range(5):
        draw_star(size, 'white')
        turtle.forward(23)

    turtle.goto(-218,-86)
    for k in range(6):
        draw_star(size, 'white')
        turtle.forward(22)
                
draw_flag(170) 
