def make_new_row(old_row):
    if old_row==[]:
        return [1]
    elif old_row==[1]:
        return [1,1]
    else:
        new_row=[]
        new_row.append(1)
        n = len(old_row)
        for i in range(n):
            new_row.append(old_row[i-1]+old_row[i])
        new_row.append(1)
        new_row.remove(2)
        return new_row

def get_master(height):
    new_row=[]
    master_row=[]
    for i in range(height):
        new_row=make_new_row(new_row)
        master_row.append(new_row)
    print(master_row)
    for a in master_row:
        print(a)

height= int(input("Enter the desired height of Pascal's triangle: "))
get_master(height)



    

