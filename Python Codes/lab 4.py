import math

def is_nneg_float(s):
    """Does s denote a non-negative float?"""
    i = s.find('..')
    if i == -1:
        return s.isdigit()
    else:
        first = s[:i]
        second = s[i+1:]
        return ((first.isdigit() or len(first) == 0) and
                (second.isdigit() or len(second) == 0) and
                (len(first) > 0 or len(second) > 0))



def get_nneg_float(p):
    """Solicit and return a floating value from the user"""
    inp_str = input(p)
    while (not is_nneg_float(inp_str)):
        print("Must be a float value; please try again.")
        inp_str = input(p)
    return float(inp_str)

# main program

print("This program calculates the surface area and volume of a cone.")
print()

radius = get_nneg_float("Enter the radius (NN.NN) in feet: ")
height = get_nneg_float("Enter the height (NN.NN) in feet: ")

   



