"""
4.3.1.8 LAB: Day of the year: writing and using your own functions

Three functions for date-related calculations: 
1. is_year_leap(year): Checks if a given year is a leap year.
2. days_in_month(year, month): Calculates the number of days in a given month, supporting leap year Februarys.
3. day_of_year(year, month, day): Calculates the day number within the year for a given date, i.e., '10' on 10th January or '366' if 31st December leap year.

Usage: Modify arguments in the bottom 'print' statement to calculate the day of the year for a specific date.
"""


def is_year_leap(year): # CHECKS IF A YEAR IS A LEAP YEAR
    if year % 4 != 0:
        return False # False = not leap year.
    elif year % 100 != 0:
        return True # True = is leap year.
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month): # CHECKS HOW MANY DAYS IN A MONTH (SUPPORTS LEAP YEAR FEBRUARYS)
    months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) is False: # If it's not a leap year:
        number_of_days = months_list[month - 1] # query list to get number_of_days.
        return number_of_days
    elif month != 2:                            # If it's a leap year but not february:
        number_of_days = months_list[month - 1] # same as above (i.e., query list...)
        return number_of_days
    else:
        number_of_days = months_list[month - 1] + 1 # For leap year februarys: same query as above + 1 extra day.
        return number_of_days

def day_of_year(year, month, day): # CHECKS DAY OF THE YEAR
    if type(year) != int or type(month) != int or type(day) != int: # Returns None if invalid.
        return None
    if month < 1 or month > 12 or year < 1: # Returns None if invalid.
        return None
    if day > days_in_month(year, month): # Returns None if month is invalid (i.e., Amaninder's february print statement below).
        return None
    
    days_in_year = 0
    for i in range(month - 1):                 # For each month up to one before the argument:
        i += 1
        days_in_year += days_in_month(year, i) # sum the result of each function call iteration.
    days_in_year += day
    return days_in_year

print(day_of_year("a", "b", "c")) # Invokes day_of_year function with year/month/day argument.
print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 2, 30))