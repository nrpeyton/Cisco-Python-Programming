'''                                   LAB: Extend Calendar Class Functionality

DIFFICULTY: Easy
TIME: 30-60 minutes

OBJECTIVES:
-Advance proficiency in Python's Calendar class.

SCENARIO:
Extend the built-in Calendar class to include a method for counting the occurrences of a specific weekday in a given year.

FEATURES:
-Create a subclass named MyCalendar that inherits from the Calendar class.
-Implement the method count_weekday_in_year with parameters year and weekday.
--year is the year in question.
--weekday is an integer between 0-6, where 0 is Monday and 6 is Sunday.
-Utilize monthdays2calendar method from the Calendar class for the implementation.
-Return the count of the specific weekday in the given year as an integer.

SAMPLE ARGUMENTS:

year=2019, weekday=0
Expected output: 52

year=2000, weekday=6
Expected output: 53

'''





import calendar

# Define a custom subclass of Python's built-in Calendar class
class MyCalendar(calendar.Calendar):

    # Implement a method to count occurrences of a specific weekday in a given year
    def count_weekday_in_year(self, year, weekday):
        count = 0
        
        # Loop through all months in the year
        for month in range(1, 13):

             # Retrieve the calendar for the given month and year. Each week is a tuple consisting of day numbers and weekday numbers. Days numbers outside the month are represented by 0.
            month_data = self.monthdays2calendar(year, month) # ***See note
            
            # Loop through each week in the month. 
            for week in month_data:
                
                # Loop through each day in the week. 
                for day in week:
                    
                    # Skip days that aren't part of the month.
                    if day[0] == 0 and day[1] == weekday:
                        continue
                    
                    # Check if the weekday matches the target weekday
                    elif day[1] == weekday:
                        count += 1
        
        return count  # Return final count

# Create an instance of MyCalendar and test the method
obj = MyCalendar()
print(obj.count_weekday_in_year(2019, 0)) # Returns 52 (correct)
print(obj.count_weekday_in_year(2000, 6)) # Returns 53 (correct)




'''

***Note to self: Always use 'self' to call parent class methods within the derived class.
This ensures that the method operates on the current instance of the object.

'''