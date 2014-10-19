print ("Martin Mukasa")
print("CSE 231 - Section: 009")
print("09/ 10/ 2012")

import math

print()

print("Calculate Garden Requirements")
print("------------------------------")

# The letters z, s, f, d where random letters that I choose to represent the
# question being asked by the program when the user enters the numbets to be calculated.

z = float(input("Enter length of side of garden (feet): "))
s = float(input("Enter spacing between plants (feet): "))
f = float(input("Enter depth of garden soil (feet): "))
d = float(input("Enter depth of fill (feet): "))

print()

# sca means = Semicirlce area
# ca means = circle area

sca = (float(((z**2)*math.pi)/32))
ca = (float(((z**2)*math.pi)/16))

print("-------------------------------")
print("Requirements for the Garden")

print()

# Description of abbreviations and what they represent:

# pscg = Plant Semicircle Garden
# pcg = Plants Circle Garden
# tpg = Total Plant Garden
# sscg = Soil Semicirlce Garden
# scg = Soil Circle Garden
# tsg = Total Soil Garden
# tfg = Total Fill Garden

pscg = int((((((z**2)*math.pi)/32))/s**2))
print ("Plants for each semicircle garden: ",pscg)

pcg = int((((((z**2)*math.pi)/16))/s**2))
print ("Plants for the circle garden: ",pcg)

# I multiply the semicirlce area by 4 to get the total area for all the 4 semicirlces.

tpg = 4*pscg+pcg
print ("Total number of plants for garden: ",tpg)

# I divided by 27 because I needed to change my answer from feet to cubic yards.

sscg = round((((sca)*f)/27),1)
print ("Soil for each semicircle garden: ",sscg, "cubic yards")

scg = round(((ca*f)/27),1)
print ("Soil for the circle garden: ",scg, "cubic yards")

tsg = round((((sca*4)+(ca))*f)/27,1)
print ("Total Soil for the garden: ",tsg, "cubic yards")

tfg = round(((z**2-((sca*4)+(ca)))*d)/27,1)
print ("Total fill for the garden: ",tfg, "cubic yards")

print()

# Explanation of functions used:

# print = used to display the test that I want to be shows when user run's the program
# import math = a function that is used which displays several math functions such as the pi than
#               entering the whole 3.14... number in the program, makes the value to be more precise.
# float = this functions is used to convert integers and strings.
# input = used as a question master that tells the user to enter something where the question is being asked.
# int = used to take any value and coverts it to an integer.
# round = this function wil round off your answer to the nearest decial that you want. E.g 3.3123 will be 3.3

print("Thank You For Using the Program")
