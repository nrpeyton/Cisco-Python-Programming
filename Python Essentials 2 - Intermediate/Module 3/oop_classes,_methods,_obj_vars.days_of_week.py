'''                                       3.4.1.13 LAB: Weeker Class for Day Manipulation

DIFFICULTY: Easy/Medium
TIME: 30-60 minutes

OBJECTIVES:
- Define classes from scratch.
- Utilise instance variables and methods.

SCENARIO:
Implement the Weeker class to store and manipulate days of the week. The constructor takes a string representing the day (Mon, Tue, etc.). An invalid input should raise a custom WeekDayError exception.

The class should:
1. Be "printable", outputting the day as a string.
2. Have methods add_days(n) and subtract_days(n) to update the stored day by n days forward or backward.

HINTS:
- Keep all object properties private.
'''


class WeekDayError(Exception):
    pass
	

class Weeker:
    weekdays_lst  = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

    def __init__(self, day):
        if day not in Weeker.weekdays_lst:
            raise WeekDayError(f"Invalid day '{day}' not in Weeker.weekdays_lst {Weeker.weekdays_lst}")
            
        self.__weekday = Weeker.weekdays_lst.index(day)

    def __str__(self):
        return Weeker.weekdays_lst[self.__weekday]

    def add_days(self, n):
        self.__weekday = n % 7 + self.__weekday

    def subtract_days(self, n):
        self.__weekday = self.__weekday - n % 7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError as e:
    print("Sorry, I can't serve your request:", e)

'''
Notes:
-Good practice using the modulus operator to loop through a tuple.
-Using tuple.index() method  allowed more concise code, as didn't need to use a 'for loop' to get the weekday index.
-Improved the error handling beyond the lab's requirements.
'''




# -Official method unveiled AFTER lab completion for comparison + reflection.  Copied below incase of future reference:
class WeekDayError(Exception):
    pass


class Weeker:
    days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.days_list.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.days_list[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
