# 4.3.1.7 LAB: How many days: writing and using your own functions
"""
This script contains two functions:
1. is_year_leap(year): Determines whether a given year is a leap year.
2. days_in_month(year, month): Calculates the number of days in a specified month of a specified year. This function takes leap years into account when calculating the number of days in February.
Additionally, the script contains a testing block that verifies the accuracy of the days_in_month(year, month) function using a set of test cases.
"""

def is_year_leap(year): # check if year is a leap year 
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True # true = is leap year
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) is False: # if it's not a leap year:
        number_of_days = months_list[month - 1] # use month parameter with list's index to get number_of_days 
        return number_of_days
    elif month != 2: # if not february, same as above
        number_of_days = months_list[month - 1]
        return number_of_days
    else:
        number_of_days = months_list[month - 1] + 1 # same as above + 1 extra day for february
        return number_of_days

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)): # (loops
	yr = test_years[i] #  through years
	mo = test_months[i] # and months)
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo) # function is called for each year/month iteration 
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")