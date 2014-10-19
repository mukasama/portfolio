number = int(input("Input an integer"))

if number < 0:
    print ("Input is negative")
elif number == 0:
    print ("It is 0")
else:
    string = ""
    quotient = 1

    while quotient != 0:
        quotient = number // 2
        remainder = number % 2
        number = quotient
        string += str(remainder) 

    print (string[::-1])
    integer=0
    power = 0
    for n in string:
        if n == '1':
            integer += 2**power
            power += 1
        elif n =='0':
            power += 1
            
    print (integer)

        
        
    
