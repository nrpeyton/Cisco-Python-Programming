'''                                     2.5.1.9 LAB: The Digit of Life

DIFFICULTY: Easy

OBJECTIVES:
- Enhance string manipulation skills.
- Convert between integers and strings.

SCENARIO:
Determine the "Digit of Life" from a user-input birthday by summing its digits. If the result has more than one digit, continue summing until a single digit remains.

TEST DATA 1                                                        TEST DATA 2
=========                                                          ==========

Sample input:       Sample output:                                 Sample input:      Sample output:

19991229            6                                              20000101           4

'''





birthday_sum = 0
digit_of_life = 0
birthday = input("Enter your birthday (YYYYMMDD): ")

for c in birthday:                      # Convert to INT to sum all the digits one at a time
    birthday_sum += int(c)

birthday_sum = str(birthday_sum)        # Convert sum back to iterable string

for c in birthday_sum:                  # Sum digits of the previous sum
    digit_of_life += int(c)

print(digit_of_life)




# Easy!