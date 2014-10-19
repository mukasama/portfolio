# Febuary/ 08/ 2013
# CSE 201, Homewwork #4
# Anthony Rogers, Martin Mukasa, Cristhofer Munoz

print range(-5,10,2)
print range(0,16,3)
print range(5,-7,-2)

def mye(k):
    '''
    This procedure starts off with importing the math library which
    we use later on. Since our n begins at 0 we sent our range
    between 0 to n+1 so it goes on adding 1 to the previous number/
    answer. We then use the factorial math name so that it returns it
    as a whole number without the point. In this example we use 6 as our k.
    '''
    import math
    n = 1
    for  i in range(0,n+1):
        t = (1./n)
        p = math.factorial(n + t)
    print
    print p
    
def ss():
    '''
    This procedure starts off by assigning all our number (0-9) with
    a variable which we call alpha. Since we want one social security
    number we set our range to 1. We assign the 9 digits in the SS# to
    a letter (a - i)as this makes it easier so that the first number
    is not a zero and just chooses the number in list x  and chooses a
    random number between 1 and 9, or the middle two digits cannot be
    99 and the last digit cannot be a 5 so that it just looks in list
    y and chooses a random number between 0 and 9 minus 5 inclusive,
    this is all done using the for function and not equal to sign. We
    then print out the SS# with the format bellow adding the first 3
    number together then the next two numbers and then the last four
    numbers. We used variables x so
    '''
    import random
    import string
    alpha = string.digits
    l = list(alpha)
    x = "123456789"
    y = "012346789"
    for i in range(1):
        a = random.choice(x)
        b = random.choice(l)
        c = random.choice(l)
        d = random.choice(l)
        e = random.choice(l)
        f = random.choice(l)
        g = random.choice(l)
        h = random.choice(l)
        i = random.choice(y)
    if (d == 9):
        (e !=9)
    if (e == 9):
        (d !=e)
    print
    print "Your SSN is ", (a + b + c) + '-' + (d + e) + "-" + (f + g + h + i)
ss()

def ONEPID():
    '''
    This procedure starts off by assigning all our number (0-9) with
    a variable which we call alpha. Since our PID starts off with the
    letter A we assign the variable P to represent our A when printing
    out the PID. We set our range to 8 because  our PID consists of 8
    digits and then generate random numbers. After we add our p which
    represented or A and s which represented our random numbers we
    generated and we added them together and got the a PID. Since the
    first number cannot be 0 we made a list called x that letter a
    randomly chooses a number between 1 - 9.
    '''
    import random
    import string
    alpha = string.digits
    l = list(alpha)
    p ="A"
    x = "123456789"
    for i in range(1):
        a = random.choice(x)
        b = random.choice(l)
        c = random.choice(l)
        d = random.choice(l)
        e = random.choice(l)
        f = random.choice(l)
        g = random.choice(l)
        h = random.choice(l)
        j = p + a + b + c + d + e + f + g + h
        print
        print 'Your MSUPID is ', j
        print


def MSUPID(k):
    '''
    This procedure is exactly the same as the previous one(ONEPID)just that
    this time we want to produce as many PIDS as we want. In this example we
    use 5 PIDs therefore our range will be set to k which will represent a
    number of PIDs we want to generate. We assign the 8 digits in the PID to
    a letter (a - j)as this makes it easier for us to worth with the restrictions
    given like the first digit of the PID cannot be a 0 and all digits cannot
    be the same like A012345678, A11111111, and A99999999.
    '''
    import random
    import string
    alpha = string.digits
    l = list(alpha)
    p ="A"
    x = "123456789"
    for i in range(k):
        a = random.choice(x)
        b = random.choice(l)
        c = random.choice(l)
        d = random.choice(l)
        e = random.choice(l)
        f = random.choice(l)
        g = random.choice(l)
        h = random.choice(l)
        j = p + a + b + c + d + e + f + g + h
        print 'Your MSUPID is ', j

mye(6)
ss()
ONEPID()
MSUPID(8000)
