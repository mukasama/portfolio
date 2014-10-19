class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):
        h = hours
        m = minutes
        s = seconds
        '''
        hours is the number of hours
        minutes is the number of minutes
        seconds is the number of seconds
        '''
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        #print(self.hours,'H')
        #print(self.minutes,'M')
        #print(self.seconds,'S')
    def str_update(self,input_str):
        '''Take a string of the form 10:20:55 (2 digits for all but hours) No return value'''
        hours,minutes,seconds=[int(n) for n in input_str.split(':')]
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        
    def print_clock(self):
        print(self.hours,'hours',self.minutes,'minutes',self.seconds,'seconds')
    def add_clocks(self,clock):
        h1 = self.hours
        m1 = self.minutes
        s1 = self.seconds
        h2 = clock.hours
        m2 = clock.minutes
        s2 = clock.seconds
        s3 = s1+s2
        mx=divmod(s3,60)
        s3 = mx[1]
        m3 = mx[0]
        m3 = m1+m2+m3
        hx = divmod(m3,60)
        m3 = hx[1]
        h3 = hx[0]
        h3 = h3 +h1+h2
        clock3 = Clock(h3,m3,s3)
        return(clock3)

clock1 = Clock(40,30,25)
clock2 = Clock(50,40,35)
string = "1234:25:33"
print('Clock1')
clock1.print_clock()
print('Clock2')
clock2.print_clock()
clock3 = clock1.add_clocks(clock2)
print('Clock3(clock1 + clock2)')
clock3.print_clock()
print('Updates Clock1')
clock1.str_update(string)
clock1.print_clock()

