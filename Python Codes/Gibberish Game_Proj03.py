# Martin Mukasa
# 09/24/ 12
# CSE 231 - 09
# Project 03

print("This program prompts the user, to enter Gibberish syllables of which are then added into the original word.")

print()

import string

while True:

    # myst1 is the first description used for the user to input first gibberish syllable they want.  
    mystr1 = input("Enter the first Gibberish syllable (add * for vowel substitute): ")

    # myst2 is the second description used for the user to input first gibberish syllable they want.
    mystr2 = input("Enter the second Gibberish syllable (add * for vowel substitute): ")

    # Your is a description used for the user to enter the word they world like to translate.
    your = input("Enter the word you would like to translate: ")

    # List of vowels when checking the user input.
    vowels = 'aeiouAEIOU'

    # The * is used as a wild card function.
    if mystr2[0] == '*':
        before = True
    elif mystr2[-1] == '*':
        before = False

    # Special case key, which checks if the previous character had been a vowel.
    the_character_before = ""

    # String is used as a function that adds everything and prints at the endd (see bellow).
    string = ""

    # When you have finished is a function used to tell if you have already made a substitution for the first character.
    when_you_have_finished = False

    # The word letter represents the letter "i" that I choose to use in the equation when adding the words. 
    for i in your:
        letter = i
        if i in vowels and when_you_have_finished == False:
            letter = mystr1 + letter
            when_you_have_finished = True

        elif i in vowels and when_you_have_finished == True:
            if the_character_before not in vowels:
                if before == False:
                    letter = mystr2 + letter
                else:
                    letter = letter + mystr2[1:] + letter 

        string = string + letter
        
    print()
    
    print(string)

    print()

    print ("Thanks for Playing!")

    print("---------------------------------------------------------------------")

    # your1 is a word I choose to represent the equation that asks the user if they want to play again or not. 
    your1 = input ("To play again type (y) or (n) to quit: ")

    if your1 == "n":
        break
    else:
        your1== "y"    
