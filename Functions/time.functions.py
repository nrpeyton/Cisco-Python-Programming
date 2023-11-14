import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

'''
OUTPUT:
I'm very tired. I have to take a nap. See you later.
 5 sec pause...▓
▒...I slept well! I feel great!
'''





import time
# or `from time import ctime`

timestamp = 1572879180
print(time.ctime(timestamp)) # Converts the time in seconds since January 1, 1970 (Unix epoch) to a string.

'''
OUTPUT:
Mon Nov  4 14:53:00 2019
'''





import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

'''
OUTPUT:
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)**
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)**
'''

# See ...Intermediate/Module 4/datetime and time modules/datetime.time & time.struct_time class constructors.txt**





import time

timestamp = 1572879180
st = time.gmtime(timestamp) # gmtime() function creates a struct_time object the same as the example above.

print(time.asctime(st)) # converts a struct_time object or a tuple to a string.  # OUTPUTS: Mon Nov  4 14:53:00 2019

print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) 
''' converts a struct_time object or a tuple that expresses the local time to the number of seconds 
since the Unix epoch. In this example, we pass a tuple to it, which consists of the following values:

2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst

OUTPUT:
1572879180.0
'''





import time

timestamp = 1572879180
st = time.gmtime(timestamp) # gmtime() function creates a struct_time object the same as the example above.

# The StringFormatTime function is the same as the dt.strftime() method (see datetime methods.txt) but additionally can also take (optionally) a tuple or struct_time object.
print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

'''
OUTPUT:
2019/11/04 14:53:00
2023/10/07 19:23:55
'''