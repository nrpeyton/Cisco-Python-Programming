def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2  # semi perimeter (p) == the sum of all sides / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5  # area == sqrt. of p * (p - a) * (p - b) * (p - c)


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))
print(area_of_triangle(1., 1., (1 ** 2 + 1 ** 2) ** .5)) # This is another way of representing the above print statement;
#                                                          included here to help with confusion.  The reason we don't simply
#                                                          write the length of side c, is because using pythagorean theorem (c² = a² + b²) 
#                                                          preserves the accuracy of the hyptotenuse in its calculation.
#                                                          Remember you still need to find the square root(²) of the hypotenuse (c in this case)
#                                                          because the hypotenuse²(SQUARED) is equal to a² + b², not just the hypotenuse without ².
