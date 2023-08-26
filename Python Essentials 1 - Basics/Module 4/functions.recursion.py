# 4.5.1.9

def factorial(n):
# Base case: factorial of 1 is 1
    if n == 1:
        return 1

    else:
        return n * factorial(n-1)     # Recursive case: n! = n * (n - 1)!

print(factorial(5))


"""
factorial(5) is called.
factorial(4) is called.     factorial(5) must wait.
factorial(3) is called.     factorial(4) must wait.
factorial(2) is called.     factorial(3) must wait.
factorial(1) is called.     factorial(2) must wait.
factorial(1) returns 1.
factorial(2) resumes, calculates 2 * factorial(1), and returns 2.
factorial(3) resumes, calculates 3 * factorial(2), and returns 6.
factorial(4) resumes, calculates 4 * factorial(3), and returns 24.
factorial(5) resumes, calculates 5 * factorial(4), and returns 120.
"""



