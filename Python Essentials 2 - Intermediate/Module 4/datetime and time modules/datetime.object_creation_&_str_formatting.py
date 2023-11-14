'''                                            4.5.1.22 LAB: strftime Method Mastery

DIFFICULTY: Easy
TIME: 15-45 minutes

OBJECTIVES:
-Enhance skills in date and time formatting using Python.
-Master the use of the strftime method and its directives.

SCENARIO:
Utilize strftime method directives to format a specific datetime object. This lab will also require consulting documentation for unknown directives.

FEATURES:
-Create a datetime object for November 4, 2020, 14:53:00.
-Use strftime method to format the datetime object in multiple ways, as specified in the 'Explain' section.

EXPLAIN:
Format the datetime object to display the following:
1. 2020/11/04 14:53:00
2. 20/November/04 14:53:00 PM
3. Wed, 2020 Nov 04
4. Wednesday, 2020 November 04
5. Weekday: 3
6. Day of the year: 309
7. Week number of the year: 44

'''







from datetime import datetime

# Note to self: Unlike many methods that are prefixed by object instances (e.g., data), strptime is a class method so is prefixed by its class name 'datetime'.
dt = datetime.strptime('2020/11/4 14:53:00', '%Y/%m/%d %H:%M:%S')
print(dt)
print(dt.strftime('%y/%B/%d %H:%M:%S %p'))
print(dt.strftime('%a, %Y %b %d'))
print(dt.strftime('%A, %Y %B %d'))
print(dt.strftime('Weekday: %u'))
print(dt.strftime('Day of the year: %j'))
print(dt.strftime('Week number of the year: %U'))





''' 
Easier/Faster way to create the datetime object:
dt = datetime(2020, 11, 4, 14, 53, 00)
'''