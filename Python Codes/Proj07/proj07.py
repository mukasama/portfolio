# Section 09 
# 10/ 29/ 2012 
# Project 07 


# The program below uses a text document called "ap_docs.txt" which contains old newswire articles.
# This document is used by a user entering a set of keywords and then finds the docuemtnt in the collection
# that matches their search term. If the user wants to display that document, they will go ahead and enter
# the document number withc will then dispalay that document. If the user doesn't want to use the program
# anymore, they will simply select 3 which will quit out of the program it opened again by the user.

import string

# This is my main program thats the first to run once the user opens the program and does the below.
def main():

    # The function below requests the user to select between the 3 posible options.
    #file is a variable assigned to my function that asks the user what they would like to do.
    file=int(input('''What would you like to do? 
    1 = Search for documents 
    2 = Read Document 
    3 = Quit Program 
    >''')) 

    while True: 
        try:
            # If the User selects "1" they will be asked to enter a search word.
            if file==1:
                # swrds = means search words (that looks in my dictonanry, which then tell what document that word is in).
                swrds=input("Enter search words: ")
                print()
                #dictionary is a variable assigned to my_dict which is my first dictionary that contains all my words in the document.
                dictionary=my_dict() 
                swrds=swrds.split()
                # es = empty set in my list.
                es=[] 
                for word in swrds:
                    if word not in dictionary:
                        setwanted=set()
                    else:
                        setwanted=dictionary[word] 
                    es.append(setwanted) 
                firstset=es[0] 
                for sets in es: 
                    firstset=firstset & sets 

                # This function is used to error check and see if the search word is in the document or not. If it is then it returns the
                # answer/ document requested. If it doesn't then the document says word not found and requests for an input again.
                if firstset == set():
                    print('Word(s) not found, please try again')
                    print()
                    main()
                    
                else:
                    setstring=str(firstset) 
                    setremovepunct=setstring.strip(string.punctuation) 
                    setremovecomma=setremovepunct.replace(',','')
                    print("Documents fitting search:" ,setremovecomma) 
                    print() 
                    main()
            # If the User selects "2" they will be asked to enter a document number. 
            elif file==2:
                # sdoc = means search document (that looks in my docs list, which then tell what document number that word is in).
                sdoc=int(input('Enter document number: ')) 
                print()
                dictionary=my_dict2() 
                print("Document #",sdoc)
                print("--------------------------------------------")
                print(dictionary[sdoc]) 
                print("--------------------------------------------") 
                main()
            # If the User selects "3" this will quit the program, till its opened again by the user to start runing. 
            elif file==3:
                quit
            # Now if the user enters none of the above numbers (1, 2, or 3) the messeage below will be displayed.
            # and the program will ask the user what they would like to do from the begining.
            else:
                print()
                print(" *** search or document not found, please try again *** ") 
                print() 
                print("--------------------------------------------") 
                file=int(input('''What would you like to do? 
    1 = Search for documents 
    2 = Read Document 
    3 = Quit Program 
    >''')) 
        except IOError: 
            print("ERROR") 
             
# My_dict = is my first dictionary which is my bigiest dictonary because it has all the words in the file.     
def my_dict():
    #docs_dict is an empty string that collects the documents in my dictionary.
    docs_dict={} 
    count=0
    #my_file is a variable assigned to my function that opens the document that the user wants to view either (ap_docs, or ap_docs2). 
    my_file=open('ap_docs.txt','r')
    #word_doc is an empty string that collects the words in my dictionary.
    word_doc=[]      
    for line in my_file: 
        line=line.strip()
        #Word_list is a variable assigned to my function that get the words in my list.
        word_list=line.split() 

        if "NEW DOCUMENT" in line: 
            count+=1 
        for word in word_list: 

            word=word.lower()
            word=word.strip(string.punctuation) 
            word_doc.append(word) 
             
            if word in docs_dict: 
                docs_dict[word].add(count) 
            else: 
                docs_dict[word]=set() 
                docs_dict[word].add(count) 
                             
    return docs_dict 

# My_dict2 = is my second dictionary which is the smaller dictionary because it has all the lines in the file.  
def my_dict2(): 
    docs_dict={} 
    count=0 
    my_file=open('ap_docs.txt','r') 
    word_doc=[] 
    ndoc='' 
    newdoc=[] 
     
    for line in my_file:  
        ndoc+=line 
    search=ndoc.split("<NEW DOCUMENT>") 
    for line in search: 
        newdoc.append(line) 
    for line in newdoc: 
        docs_dict[count]=line 
        count+=1 
    return docs_dict 

main()
