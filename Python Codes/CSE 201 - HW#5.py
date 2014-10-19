# Febuary/ 14/ 2013
# CSE 201, Homewwork #5
# Anthony Rogers, Cristhofer Munoz, Martin Mukasa

def str2num(s):
    '''
    This procedure starts off by importing sting then assigning our upper and
    lower case letters to a variable. In this case we use alpha for upper case
    and beta for lower case letters. We then have to present our alpha and beta
    letters into a list of variable so that it make it easier for python to
    search for. This is where we set two other variable called DELTA and SIGMA
    and then use the variable called OMEGA to add the two. We then list our
    numbers from 00 - 51 to represent the upper and lower case letter. From there
    we set up an digit that will add all out variables asked for in (s), that it
    later return. We then use the for function as it goes through the loop to
    see which word is asked for in (s), finds each letter and its corresponding
    number/ digit and then returns the digits/ number for each letter in the word
    typed in.
    '''
    import string
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    DELTA = list(alpha)
    SIGMA = list(beta)
    OMEGA = DELTA + SIGMA
    num = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51"]
    digit = ""
    for letter in s:
            for k in range(len(OMEGA)):
                if letter == OMEGA[k]:
                    k = num[k]
                    digit = digit + str(k)
    
    return digit
    print


def str2numsp(s):
    '''
    This procedure is very similar to the first code, just that this time we are
    asked to add in two more values which are the space and period between the
    word being presented to us. Without repeating everything in the first code
    above, we then list our numbers from 00 - 51 to represent the upper and lower
    case letter and then add on 52 and 53 too represents the space and period.
    It goes through the loop to see which word is asked for in (s), finds each
    letter, space and period with its corresponding number/ digit and then
    returns the digits/ number for each letter, space and period in the word
    typed in.
    '''
    import string
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    DELTA = list(alpha)
    SIGMA = list(beta)
    space = " "
    period = "."
    Lspace = list(space)
    Lperiod = list(period)
    OMEGA = DELTA + SIGMA + Lspace + Lperiod
    num = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53"]
    digit = ""
    for letter in s:
            for k in range(len(OMEGA)):
                if letter == OMEGA[k]:
                    k = num[k]
                    digit = digit + str(k)
                        
    print 
    return digit 
    print

def num2str(s):
    '''
    This procedure is very similar to the second code above, just that this time
    we are asked the opposite. We are given numbers and asked to return the
    word in those numbers. Using the second code we just change were we had OMEGA
    to num and then digit to letters. It then goes through the same loop as in the
    code above. Finds the numbers/ digits typed in (s) assigns it to the corresponding
    letter then returns letter, space and period in the number/ digits typed in.
    '''
    import string
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    DELTA = list(alpha)
    SIGMA = list(beta)
    space = " "
    period = "."
    Lspace = list(space)
    Lperiod = list(period)
    OMEGA = DELTA + SIGMA + Lspace + Lperiod
    num = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53"]
    letters = ""
    for number in s:
            for k in range(len(num)):
                if number == num[k]:
                    k = OMEGA[k]
                    letters = letters + str(k)
     
    return letters
    print


def perf(n):
    '''
    This procedure is shorter than the other ones because we are asked to say if
    the positive integer given in perfect or not. We begin by assigning our sum
    equal to 0 and then create a for function that goes through the loop. If the
    positive integer is equal to the sum of its integer divisors, except itself
    it is considered perfect therefore Yes is returned and if not therefore No
    will be returned.
    '''
    sum = 0
    for p in range(1,n):
        if n%1 == 0:
            sum = sum + p 
            if sum == n:
                return "Yes"
            if sum != n:
                return "No"

print str2num('Thepriceofgreatnessisresponsibility')
print str2numsp('Growing old is inevitable but growing up is optional.')
print num2str('5014205232141952341953')
print perf(945)
               

