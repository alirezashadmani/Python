class Time:
    
    def __init__(self,hour,minute,second):  #initialize 
        self.hour = hour
        self.minute = minute
        self.second = second

    """def __add__(self,other):                #Add+
        hour = self.hour + other.hour
        minute = self.minute + other.minute
        second = self.second + other.second

        if second >= 60:
            second = second - 60
            minute = minute + 1
        if minute >=60:
            minute = minute - 60
            hour = hour + 1

        return Time(hour,minute,second)
##################################################
    def __sub__(self,other):                #subtract-
        hour = self.hour - other.hour
        minute = self.minute - other.minute
        second = self.second - other.second

        if second < 0:
            print('error')
        elif second >= 60:
            second = second - 60
            minute = minute + 1
        if minute < 0:
            print('error')
        elif minute >=60:
            minute = minute - 60
            hour = hour + 1
        return Time(hour,minute,second)"""
##################################################
    def __eq__(self,other):                #equal=
        if t1 == t2:
            print('Time match')
        else:
            print('Time does not match')

    def __le__(self,other):                #lower_equal <=
        if t1 <= t2:
            print('First time is lower')
        else:
            print('Second time is lower')

    def __ge__(self,other):                #greater_equal <=
        if t1 >= t2:
            print('First time is greater')
        else:
            print('Second time is greater')


    def __str__(self):                      #string representation
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
        
    
    def __repr__(self):                     #represent
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)

    
    def show(self):                         #show
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)
    
            
            



    
