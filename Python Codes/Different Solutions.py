print range(-5, 10, 2)
print range(0,17, 3)
print range(5, -6,-2)

def mye(k):
    '''
    Computes e up to k terms of the series
    '''
    import math
    e = 0
    for i in range(k):
        e = e + 1./math.factorial(i)
    print e
    
    
def ss():
    '''
    Generates a restricted random ss
    '''
    import string
    import random
    s09 = string.digits
    sn0 = s09[1:]
    sn9 = s09[:-1]
    sn5 = s09[:5] + s09[6:]

    #print s09, sn0, sn9, sn5

    s = random.choice(sn0)
    for i in range(2):
        s = s + random.choice(s09)
    s = s + '-'
    for i in range(2):
        s = s + random.choice(sn9)
    s = s + '-'
    for i in range(3):
        s = s + random.choice(s09)
    s = s + random.choice(sn5)
    print s


def ONEPID():
    '''
    prints one PID with some restrictions
    '''
    import random
    
    while True:
        pid = random.randint(10000000, 99999999)
        if pid % 11111111 != 0:
            break
    #print 'A' + str(pid)
    return pid

def MSUPID(k):
    pidlist=[]
    while len(pidlist) < k:
        pid = ONEPID()
        if pid in pidlist:
            continue
        else:
            pidlist.append(pid)
    for pid in pidlist:
        print 'A' + str(pid)


def MSUPID_ver01(k):
    '''
    Prints out k random MSU PIDs with some restrictions
    '''
    import random
    sL = []     #making a list of forbidden numbers
    for i in range(1,10):
        sL.append(11111111*i)
        
    #print sL
    
    pid_list = []
    
    loopCount = 0
        
    while len(pid_list) != k:
        pid = random.randint(10000000, 99999999)
        loopCount = loopCount + 1
        if pid in pid_list or pid in sL:
            continue
        pid_list.append(pid)
    for id in pid_list:
        print 'A'+ str(id)
    print 'Loop Count is ', loopCount

 

def MSUPID_ver02(k):
    '''
    Prints out k random MSU PIDs with some restrictions
    '''
    import random
    
    pid_list = []
    
    loopCount = 0
        
    while len(pid_list) != k:
        pid = random.randint(10000000, 99999999)
        loopCount = loopCount + 1
        if pid % 11111111 != 0 and pid not in pid_list:
            pid_list.append(pid)
    for id in pid_list:
        print 'A'+ str(id)
    print 'Loop Count is ', loopCount

mye(6)
ss()
ONEPID()
MSUPID(5)
