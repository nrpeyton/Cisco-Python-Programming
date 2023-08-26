"""
4.5.1.4 Creating functions | testing triangles | Pythagorean theorem

This script checks whether given lengths can form a right triangle (c2 = a2 + b2).
"""


def is_a_triangle(a, b, c): # Function to check if lengths a, b, c can form a triangle
    return a + b > c and b + c > a and c + a > b # Returns True if any two sides are longer than the remaining side (required for a triangle). Otherwise False.


def is_a_right_triangle(a, b, c): # Function to check if lengths a, b, c can form a right triangle
    if not is_a_triangle(a, b, c): # Starts by invoking is_a_triangle function to instantly return False if a triangle can't be formed.
        return False
    # We check for the longest side, which is used in applying (i.e., checking) Pythagorean theorem.
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(is_a_right_triangle(5, 3, 4)) # Test the function with lengths that form a right triangle
print(is_a_right_triangle(1, 3, 4)) # Test the function with lengths that don't form a right triangle
