import string
#3) Returns string s in reverse
def rev(s):
    t = ''
    s = s[::-1]
    return s

#4) Return yes or no if string s has a duplicate character
def dup(s):
    alpha = ('abcdefghijklmnopqrstuvwxyz')
    if s in alpha:
        return 'Yes'
    else:
        return 'No'

#5) Returns a list containing all the divisors of integer n.
def prime(n):
    for x in xrange(2, int(n**0.5)+1):
        if n % x == 0:
            return 'No'
    return 'Yes'

#6) Returns a random k-digit palindorme.
def pld(k):
  if k[0] == k[-1]:
    return 'True'
  elif k[0] == k[-1] and k[1] == k[-2] :
    return 'True'
  else:
    return 'False'

#7) Prints out the first n numbers in the Fibonacci Sequence.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

#9) Returns true or false if it is a leap year.
def leap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
    
#10) Go State function prints numbers from 1 to 100.
def GoState(x):
    if x % 3 == 0:
        return 'Go'
    if x % 5 == 0:
        return 'State'
    if x % 5 == 0 and x % 3 == 0:
        return 'GO State'
    print 'Go State' range(1,100,1)

#8) Prints out a string s, three characters at a time.
def printthree(s):
