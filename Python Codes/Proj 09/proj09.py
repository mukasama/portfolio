# CSE 231 Section 009 
# 10/ 15/ 2012 
# Project 09

import string

def main1():
    
    file1 = open('BLS_private.csv', 'r') 

    for i in range(12): 
        file1.readline()
        
    count=0
    my_file = []
    for line in file1:
        line = line.strip()
        lines = line.split(',')
        my_file.append(lines)

    file1.close()
    return(my_file)
    
def main2():

    file2 = open('presidents.txt','r')

    count=0
    my_files = []
    
    for line in file2:
        line = line.strip()
        lines = line.split('\t')
        my_files.append(lines)

    file2.close()
    return(my_files)
    
   
def compare():
    my_file=main1()
    my_files=main2()
    demo=[]
    rep=[]
    for line in my_files:
        name=line[0]
        monthofe=int(line[1])
        yearofe=int(line[2])-1961
        monthofl=int(line[3])
        yearofl=int(line[4])-1961
        party=line[5]
        jobate=my_file[yearofe][monthofe]
        jobatl=my_file[yearofl][monthofl]
        job=int(jobatl)-int(jobate)
        jobs=(float(job/1000))
        if jobs>0:
            linetoadd=name+': Increase of ' + str(jobs) + ' jobs'
        else:
            linetoadd=name+': Decrease of ' + str(abs(jobs)) + ' jobs'
        if party=='Democratic':
            d=[]
            d.append(linetoadd)
            d.append(jobs)
            demo.append(d)
        elif party == 'Republican':
            r=[]
            r.append(linetoadd)
            r.append(jobs)
            rep.append(r)
        else:
            pass
    print("Republicans")
    print(" ")
    for i in rep:
        print(i[0])
    print(" ")
    print("Democrats")
    print(" ")
    for i in demo:
        print(i[0])

    reptotal=0
    demototal=0
    for i in rep:
        x=i[1]
        reptotal+=x
    for i in demo:
        x=i[1]
        demototal+=x
    print(" ")
    print("Total increase by Republicans: ", reptotal)
    print(" ")
    
    print("Total increase by Democrats: ", demototal)
    print(" ")
    if demototal>reptotal:
        print("So Clinton was right")
    else:
        print("So Clinton was wrong")
    
    
compare()
main1()
main2()
            
        

