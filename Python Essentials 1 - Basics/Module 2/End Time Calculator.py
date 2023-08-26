"""
Problem:
    Given the start time of an event and its duration, calculate the end time.
    
Approach:
    Convert the start time to minutes, add the duration, then convert back to hours and minutes.
    The modulo operator (%) is used to calculate the minutes left over when converting back; and also, to handle times that cross over midnight.
    
Inputs:
    Starting time (hours): An integer between 0 and 23.
    Starting time (minutes): An integer between 0 and 59.
    Event duration (minutes): An integer which could be arbitrarily large.
    
Outputs:
    Prints the end time in the format "hours:minutes".
    
Test Cases:
    Test Case 1:
        Input: 12, 17, 59
        Output: 13:16
        
    Test Case 2:
        Input: 23, 58, 642
        Output: 10:40
        
    Test Case 3:
        Input: 0, 1, 2939
        Output: 1:0
"""

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Convert start time to minutes
start_time_in_minutes = (hour * 60) + mins

# Add the duration (minutes) to the start time (converted to minutes)
end_time_in_minutes = start_time_in_minutes + dura

# Convert from minutes to hours, then, determine the minutes left over
end_time_in_hours = end_time_in_minutes // 60
minutes_left_over = end_time_in_minutes % 60

# Convert hours for 24hr clock
clock_24hour = end_time_in_hours % 24

print(clock_24hour,minutes_left_over,sep=":")
