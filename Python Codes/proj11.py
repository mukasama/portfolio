# CSE 231 - Section 009  
# 12/ 05/ 2012  
# Project 11 

import string
import urllib.request
import math

# This program simply uses the calculator API for purposes of converting currencies. As with all iGoogle API's,
# it is based on creating a query using the http protocol of the web. As with all iGoogle API's, it is based on
# creating a query using the http protocol of the web.

class Currency():

    # This function takes the takes the following arguments (an amount, and the default currency).
    def __init__(self,amount=1, def_curr='USD'):
        self.amount=amount
        self.def_curr=def_curr

    # This function takes a single argument, a currency code, with no default.
    # It returns a new Currency object with the new currency code and the converted amount.
    def convert_to(self, t):
        # This is the API calculator website that converts all my currencies.
        web_obj = urllib.request.urlopen("http://www.google.com/ig/calculator?hl=en&q="+str(self.amount)+self.def_curr+"=?"+t)
        results_str = str(web_obj.read())
        web_obj.close()

        results_str = results_str.split()
        new_curr = results_str[3].strip("\"")
        
        return Currency(float(new_curr),t)

    # This return the amount and type as a string it also does error checking to see wheather or not
    # the currency listed it available. If currency is not one of the 10 then return an error message.
    def __str__(self):
        if self.def_curr not in 'USD, EUR, GBP, CAD, AUD, INR, THB, CNY, AED, CHF':
            return 'Error curreny type not found'
        else:
            return str(self.amount)+" "+str(self.def_curr)

    # This function adds two currency and return the answer e.g. 1 + 2 = 3.  
    def __add__(self, f):
        
        if type(f) == int:
            newx = self.amount + f
            return Currency(newx,self.def_curr)

        if type(f) == float:
            newx = self.amount + f
            return Currency(newx,self.def_curr)
        
        curr_conv = f.convert_to(self.def_curr)
        new_x = self.amount + curr_conv.amount
        return Currency(new_x, self.def_curr)
    
    # This function is exactly similar to the adds function just that this time it flips the numbers over
    # for example 2 + 1 = 3. 
    def __radd__(self, f):
        return self.__add__(f)

    # This function subtracts two currency and return the answer e.g. 2 - 1 = 1.
    def __sub__(self, f):
        
        if type(f) == int:
            newx = self.amount - f
            return Currency(newx,self.def_curr)

        if type(f) == float:
            newx = self.amount - f
            return Currency(newx,self.def_curr)
        
        curr_conv = f.convert_to(self.def_curr)
        new_x = self.amount - curr_conv.amount
        return Currency(new_x, self.def_curr)

    # This function is exactly similar to the subtraction function just that this time it flips the numbers
    # over for example 1 - 2 = -1. 
    def __rsub__(self, f):

        if type(f) == int:
            newx = f - self.amount
            return Currency(newx,self.def_curr)

        if type(f) == float:
            newx = f - self.amount 
            return Currency(newx,self.def_curr)
        
        curr_conv = f.convert_to(self.def_curr)
        new_x = curr_conv.amount - self.amount
        return Currency(new_x, self.def_curr)
        return self.__rsub__(f) 

    # This function does the greather than calculation.             
    def __gt__(self,f): 
        if type(f) == int:
            #If one amount is greater than the other then it will return true e.g. 2 > 1 = TRUE.
            return self.amount > f

        if type(f) == float:
             #If one amount is not greater than the other then it will return false e.g. 1 > 2 = FALSE.
            return self.amount > f

        curr_conv = f.convert_to(self.def_curr)
        return self.amount > curr_conv.amount

    # This function does the less than calculation. 
    def __lt__(self,f): 
        if type(f) == int:
            #If one amount is less than the other then it will return true e.g. 1 < 2 = TRUE.
            return self.amount < f

        if type(f) == float:
            #If one amount is not less than the other then it will return false e.g. 2 < 1 = FALSE.
            return self.amount < f

        curr_conv = f.convert_to(self.def_curr)
        return self.amount < curr_conv.amount
                                                   
    def __repr__(self):
        return self.__str__() 

# This is my main function that tests all the functions to see if they work well.                              
def main():

    print()
    print('''This program simply uses the calculator API for purposes
of converting currencies.''')
    print("----------------------------------------------------------")
    print()
    
    curr = Currency(7.50, 'USD')
    print('The first amount and currency you are converting to is: ',curr)
    print()
    curr2 = Currency(2, 'EUR')
    print('The second amount and currency you are converting to is: ',curr2)
    print()
    # This is where you can change the currency to convertor out of the 10 listed above which are:
    # USD, EUR, GBP, CAD, AUD, INR, THB, CNY, AED, CHF.
    new_curr = curr2.convert_to('USD')
    print('The amount you are converting to is: ',new_curr,'with the currency.')
    print()
    sum_curr = curr + curr2
    print('This answer has shows the addition of your first & second amount and currency: ',sum_curr)
    print()
    sum_curr1 = curr - curr2
    print('This answer has shows the subtraction of your first & second amount and currency: ',sum_curr1)
    print()
    sum_curr2 = curr + 5.5
    print('This answer has shows the addition of your first & your floating number e.g (5.5): ',sum_curr2)
    print()
    sum_curr3 = curr > 10
    print('This answer has shows if your first currency is greater than the number user has input: ',sum_curr3)
    print()
    sum_curr4 = curr < 10
    print('This answer has shows if your first currency is less than the number user has input: ',sum_curr4)
    print()
    sum_curr5 =(5 + Currency(20,'USD'))
    print('''This answer has shows if radd function as it adds the first amount the user puts in
then the second amount and the currency they would like to calculate: ''',sum_curr5)
    print()
    sum_curr6 =(5 - Currency(20,'USD'))
    print('''This answer has shows if radd function as it subtracts the first amount the user puts in
then the second amount and the currency they would like to calculate: ''',sum_curr6)
    print()
    sum_curr7=(Currency(7.50, 'XYZ'))
    print('This answer shows an error because the currency that the user has input is not valid or listed: ',sum_curr7)
main()

# Its been such a great experince in this class although started off preety rough with the project
# but I have managed to learn more and more about python and look forward to use it more in the future
# Thanks for all the help. Martin Mukasa.
