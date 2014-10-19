# CSE 231 Section 009 
# 10/ 15/ 2012 
# Project 05


import string


def minmax(new_list,cause):
    # Listofdiseases is just a word I choose to complet my function.
    listofdiseases=[] 
    for disease in cause: 
        column=[]
        # new_list 
        for row in new_list:
            # The (newnum, nos, noNA, noflt and nornd) are just words assigned to describe my formula's on the right.
            newnum=row[disease] 
            nos=newnum.replace('%','') 
            noNA=nos.replace('N/A','0') 
            noflt=float(noNA) 
            nornd=round(noflt,1) 
            column.append(nornd) 

            # text and row are just words I choose to complet my function(s) bellow.
            text=[] 
            for row in new_list: 
                st=row[0] 
                text.append(st)
            # column goes into the spreedsheet which then goes throw each column and finds the max and min values along with there states.
            def find_max(column,text): 
                max_number = float(0.0) 
                state = '' 
                count=0 
                while count < 51: 
                    if column[count] > max_number: 
                        max_number = float(column[count]) 
                        state = text[count] 
                    else: 
                        max_number=max_number 
                    count=count+1 
                return state,max_number 
        x = find_max(column,text) 


        maximum=float(x[1]) 
        def find_min(column,text): 
            min_number = maximum 
            state = '' 
            count=0 
            while count < 51: 
                if column[count] < min_number: 
                    min_number = float(column[count]) 
                    state = text[count] 
                else: 
                    min_number=min_number 
                count=count+1 
            return state,min_number 
        y = find_min(column,text) 
        listofdiseases.append(y) 
        listofdiseases.append(x) 
         
    return (listofdiseases)

def main():
    
    # filename is a name given to the function that requests the user to enter the file they would like to open. 
    filename = input("Enter the name of the input file: ") 
    while True: 
        try: 
    # fileobj is a name givein to the function that opens the file the user requested for, then reads and displays the file.  
            fileobj = open(filename, "r") 
            break 
        except IOError: 
            print('Error file not found! ') 
            filename = input("Enter the name of the input file: ") 


    # Lis is just a word i choose to complet my function to append my values.
    for lis in z: 
        for string in lis: 
            completelist.append(string) 

    # hd stands for Heart Disease Death Rate in 2007. 
    hd=[['Heart Disease Death Rate (2007)'],[completelist[0]],[str(completelist[1])],[completelist[2]],[str(completelist[3])]] 

    # mv stands for Motor Vehicle Death Rate in 2009. 
    mv=[['Motor Vehicle Death Rate (2009'],[completelist[4]],[str(completelist[5])],[completelist[6]],[str(completelist[7])]] 

    # tb stands for Teen Birth Rate in 2009. 
    tb=[['Teen Birth Rate (2009)'],[completelist[8]],[str(completelist[9])],[completelist[10]],[str(completelist[11])]] 

    # asm stands for Adult Smoking in 2010. 
    asm=[['Adult Smoking (2010)'],[completelist[12]],[str(completelist[13])],[completelist[14]],[str(completelist[15])]] 

    # ao stands for Adult Obesity in 2010. 
    ao=[['Adult Obesity (2010)'],[completelist[16]],[str(completelist[17])],[completelist[18]],[str(completelist[19])]] 

    print(hd) 
    print(mv) 
    print(tb) 
    print(asm) 
    print(ao)    

    fileobj.close() 

    # Endfile is a the name of the file I used to open the txt file.
    endfile=open('best_and_worst.txt','w')
    # Endfile.write wirtes the printed text from the python shell windown onto the txt file.
    endfile.write('') 
    endfile.write("{:31s} : {:35s}  {:20s}".format("Indicator","Min","Max")) 
    endfile.write("\n") 
    endfile.write("{}".format("-"*102)) 
    endfile.write("\n") 

    endfile.write("{:31s} : {:23s} {:10s}   {:23s} {:23s}\n".format(hd[0][0],hd[1][0],hd[2][0],hd[1][0],hd[4][0])) 
    endfile.write("{:31s} : {:23s} {:10s}   {:23s} {:23s}\n".format(mv[0][0],mv[1][0],mv[2][0],mv[1][0],mv[4][0])) 
    endfile.write("{:31s} : {:23s} {:10s}   {:23s} {:23s}\n".format(tb[0][0],tb[1][0],tb[2][0],tb[1][0],tb[4][0])) 
    endfile.write("{:31s} : {:23s} {:10s}   {:23s} {:23s}\n".format(asm[0][0],asm[1][0],asm[2][0],asm[1][0],asm[4][0])) 
    endfile.write("{:31s} : {:23s} {:10s}   {:23s} {:23s}\n".format(ao[0][0],ao[1][0],ao[2][0],ao[1][0],ao[4][0])) 

    endfile.close()

main() 
