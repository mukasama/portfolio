words = open('wordList.txt', 'r')

def anagram_sort(x):
    myList = list(x)
    myList.sort()
    sortedString = ''.join(myList)
    return sortedString



def make_dict():
    v_dict = {}
    for line in words:
        line = line.strip()
        line = line.lower()
        if line[0] == 'v':
            v_dict[anagram_sort(line)] = line
    return v_dict
    
def anagram(y):
    y = anagram_sort(y)
    x = t[y]
    print(x)


t = make_dict()
anagram('serve')
anagram('rival')
anagram('lovely')
anagram('caveat')
anagram('devote')
anagram('irving')
anagram('livery')
anagram('selves')
anagram('latvian')
anagram('saviour')
anagram('observe')
anagram('octavian')
anagram('dovetail')
anagram('levantine')

myList = [(2,300),(17,400),(1,600),(4,1100)]
myList.sort()
print(myList)
##
##myList = [('c',5),('a',9),('a',2),('b',8),('c',8), ('c',)]
##myList.sort()
##print(myList)
