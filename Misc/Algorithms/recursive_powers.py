def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def power(x, n):
    print("Computing", x, "raised to power", n, ".")
    # base case
    if n == 0:
        return 1
    
    # recursive case: n is negative
    if n < 0:
        return 1 / power(x, -n)
    
    # recursive case: n is odd
    if is_odd(n) == True:
        return x * power(x, n - 1)
    
    # recursive case: n is even
    if is_even(n) == True:
        y = power(x, n / 2)
        return y * y
        

def display_power(x, n):
    print(x, "to the", n, "is", power(x, n))

# Uncomment these lines to test your function
display_power(3, 0)
assert power(3, 0) == 1, "3 to the power of 0 should be 1"

display_power(3, 1)
assert power(3, 1) == 3, "3 to the power of 1 should be 3"

display_power(3, 2)
assert power(3, 2) == 9, "3 to the power of 2 should be 9"

display_power(3, -1)
assert power(3, -1) == 1/3, "3 to the power of -1 should be 1/3"

display_power(2, -3)
assert power(2, -3) == 0.125, "2 to the power of -3 should be 0.125"

display_power(2, -4)
assert power(2, -4) == 0.0625, "2 to the power of -4 should be 0.0625"

display_power(5, 4)
assert power(5, 4) == 625, "5 to the power of 4 should be 625"

display_power(10, 10)
# assert power(10, 10) == 10000000000, "10 to the power of 10 should be 10000000000"

display_power(5, -4)
from math import isclose
assert isclose(power(5, -4), 1/625), "5 to the power of -4 should be 1/625," # rounding error?? <--- fixed ✓

