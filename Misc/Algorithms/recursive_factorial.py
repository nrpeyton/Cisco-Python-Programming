def factorial(n):                           # SEE DIAGRAMS IN: .../Education/Comp Science/
    # base case
    if n == 0:
        return 1
    
    return n * factorial(n-1)

# Test the function
print("The value of 0! is " + str(factorial(0)) + ".")
print("The value of 3! is " + str(factorial(3)) + ".")
print("The value of 5! is " + str(factorial(5)) + ".")
print("The value of 6! is " + str(factorial(6)) + ".")

# Uncomment the lines below once you implement the recursive case
assert factorial(0) == 1, "Test for 0! failed"
assert factorial(3) == 6, "Test for 3! failed"
assert factorial(5) == 120, "Test for 5! failed"
assert factorial(6) == 720, "Test for 6! failed"


""" 3!
factorial(3):
    n3 * factorial(n-1); factorial(2):
        n2 * factorial(n-1); factorial(1):
            n1 * factorial(n-0); factorial(0):
                return 1
            n1 * 1 = 1
        n2 * 1 = 2
    n3 * 2 = 6

"""

# Diagram: /media/nick/OCZ-VERTEX4/Backup/Education/Computer Science