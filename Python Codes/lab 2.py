import turtle
import time


n = int(input("Enter the number of sides for the polygon: "))

print(n)

turtle.down()

r=int(input("Enter amount of red: "))
if r<0 or r>1:
    print("Number not between or equal to 0 and 1. Run Program again.")
g=int(input("Enter amount of green: "))
if g<0 or g>1:
    print("Number not between or equal to 0 and 1. Run Program again.")
b=int(input("Enter amount of blue: "))
if b<0 or b>1:
    print("Number not between or equal to 0 and 1. Run Program again.")

turtle.begin_fill()

for i in range(n):

    turtle.color(r,g,b)
    turtle.forward(100)
    turtle.right(180-(180*(n-2))/n)

turtle.end_fill()

turtle.up()
turtle.goto(0, 250)

turtle.down()
turtle.begin_fill()

count=0
while count < n:
    count= count+1

    turtle.color(r,g,b)
    turtle.forward(100)
    turtle.right(180-(180*(n-2))/n)

turtle.end_fill()
