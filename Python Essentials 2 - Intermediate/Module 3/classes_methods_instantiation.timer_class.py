'''                                       3.4.1.12 LAB: Timer Class for Rocket Launch

DIFFICULTY: Easy/Medium
TIME: 30-60 minutes

OBJECTIVES:
- Define classes from scratch.
- Utilize instance variables and methods.

SCENARIO:
Develop a Timer class to count seconds with specific functionalities. This class is critical as it will be used in international rocket missions to Mars.

The Timer constructor should take hours, minutes, and seconds, all with default values of zero. The class should:

1. Be "printable", outputting time in "hh:mm:ss" format with leading zeros.
2. Implement methods next_second() and previous_second() to increment/decrement time by 1 second.

HINTS:
- Keep all object properties private.
- Consider a separate function for time string formatting.
'''



def prefixer(s):
    if len(s) == 1:
        s = '0' + s
        return s
    else:
        return s



class Timer:
    def __init__(self, hours = 0, mins = 0, secs = 0):
        self.__hours = hours
        self.__mins = mins
        self.__secs = secs


    
    def __str__(self):
        h = str(self.__hours)
        m = str(self.__mins)
        s = str(self.__secs)
        
        hh = prefixer(h)
        mm = prefixer(m)
        ss = prefixer(s)

        string = hh + ':' + mm + ':' + ss
        return string


    def next_second(self):
        
        self.__secs += 1
        
        if self.__secs == 60:
            self.__secs = 0
            self.__mins += 1
            
        if self.__mins == 60:
            self.__mins = 0
            self.__hours += 1
        
        if self.__hours == 24:
            self.__hours = 0


    def prev_second(self):
        pass
        #
        # still to write this bit
        #



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)





# No help or notes required at all.  However, did compare solution elegance and realised my next_second() method could be more elegant; see below:

''' Wrap-Around Alternative for next_second()

    def next_second(self):
        self.__secs = (self.__secs + 1) % 60
        if self.__secs == 0:
            self.__mins = (self.__mins + 1) % 60
            if self.__mins == 0:
                self.__hours = (self.__hours + 1) % 24
'''