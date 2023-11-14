from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

'''
OUTPUT:
366 days, 0:00:00
365 days, 9:07:00
'''




                                                # CREATING TIMEDELTA OBJECTS

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

'''
OUTPUT:
16 days, 3:00:00
'''





from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

'''
OUTPUT:
Days: 16
Seconds: 10800
Microseconds: 0
'''





from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

'''
OUTPUT:
16 days, 2:00:00
32 days, 4:00:00
2019-11-05
2019-11-05 18:53:00
'''