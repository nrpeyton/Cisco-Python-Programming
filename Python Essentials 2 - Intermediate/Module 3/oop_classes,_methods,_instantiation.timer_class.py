'''                                       3.4.1.12 LAB: Timer Class for Rocket Launch

DIFFICULTY: Easy/Medium
TIME: 30-60 minutes

OBJECTIVES:
- Define classes from scratch.
- Utilise instance variables and methods.

SCENARIO:
Develop a Timer class to count seconds with specific functionalities. This class is critical as it will be used in international rocket missions to Mars.

The Timer constructor should take hours, minutes, and seconds, all with default values of zero. The class should:

1. Be "printable", outputting time in "hh:mm:ss" format with leading zeros.
2. Implement methods next_second() and previous_second() to increment/decrement time by 1 second.

HINTS:
- Keep all object properties private.
- Consider a separate function for time string formatting.

EXPECTED OUTPUT:
23:59:59
00:00:00
23:59:59
'''



class Timer:
    def __init__(self, hrs = 0, mins = 0, secs = 0):
        self.__hours = hrs
        self.__minutes = mins
        self.__seconds = secs

    def __str__(self):
        clockstr = format_string(self.__hours) + ':' + format_string(self.__minutes) + ':' + format_string(self.__seconds)
        return clockstr

    def next_second(self):
        self.__seconds = (self.__seconds + 1) % 60
        if self.__seconds == 0:
            self.__minutes = (self.__minutes + 1) % 60
            if self.__minutes == 0:
                self.__hours = (self.__hours + 1) % 24
                    
    def prev_second(self):
        self.__seconds = (self.__seconds - 1) % 60
        if self.__seconds == 59:
            self.__minutes = (self.__minutes - 1) % 60
            if self.__minutes == 59:
                self.__hours = (self.__hours - 1) % 24


def format_string(t):
    if t < 10:
        return '0' + str(t)
    else:
        return str(t)
    
    
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)





# No help or notes were needed, and while an alternative non-modulus method for time wrapping was considered (shown below), my current modulus approach (above) is more elegant.

''' Less elegant solution for next_second()

self.__secs += 1

if self.__secs == 60:
    self.__secs = 0
    self.__mins += 1
    
if self.__mins == 60:
    self.__mins = 0
    self.__hours += 1

if self.__hours == 24:
    self.__hours = 0

'''