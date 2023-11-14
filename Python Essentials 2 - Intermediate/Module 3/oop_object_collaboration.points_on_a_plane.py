'''                                       3.4.1.14 LAB: Points on a Plane

OBJECTIVES:
- Define classes from scratch.
- Utilise instance variables and methods.

SCENARIO:
Create a Point class to store x and y coordinates as floats and calculate distances between points on a Cartesian plane. Leverage the math module's hypot() function for calculating distances.

The class should:
1. Have a constructor accepting two arguments (x and y), both defaulting to zero.
2. Keep all properties private.
3. Include getx() and gety() methods to return each coordinate.
4. Offer distance_from_xy(x,y) method to calculate distance from another point provided as floats.
5. Offer distance_from_point(point) method to calculate distance from another Point object.

'''



import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x  # Initialize x-coordinate of this Point object
        self.__y = y  # Initialize y-coordinate of this Point object

    def getx(self):
        return self.__x  # Retrieve x-coordinate of this Point object

    def gety(self):
        return self.__y  # Retrieve y-coordinate of this Point object

    def distance_from_xy(self, x, y):
    # Computes distance from the point represented by this instance (self) to another point specified by (x, y) coordinates.
    # The first print statement in main uses this to calculate the distance between 'point1' object (self) and 'point2 object'.
    # The last print statement calculates the distance from 'point2' to arbitrary coordinates (2, 0), independent and seperately of the first print statement.
        return math.hypot(self.__x - x, self.__y - y)  # Compute distance from own object's point to another point (i.e., point 1 object to point2 object with the first print statement.  And then totally seperately, with the last print statement, calculate distance from point 2 object to the given (arbitrary) x, y coordinates. FOR FUTURE REFERENCE (as this took me a while to figure out): Remember, that with the second last print statement, Self.__x and self.__y are point1, and x and y are point 2.

    def distance_from_point(self, point):
        # Compute distance from this Point object to another Point object by using their x, y coordinates
        return self.distance_from_xy(point.getx(), point.gety())  

# Instantiate Point objects
point1 = Point(0, 0)
point2 = Point(1, 1)

# Calculate distance between point1 and point2 using their Point objects
print(point1.distance_from_point(point2)) # 'point2' is passed as an entire object to get permission to use its methods like point.getx() in the function.


# Calculate distance from point2 to specific x, y coordinates (2, 0)
print(point2.distance_from_xy(2, 0))



'''                                                 N O T E S

PERSONAL:
This was difficult, main takeaways/learnings:

OBJECTS AS ARGUMENTS:
Methods of an object can accept other objects as arguments, allowing for direct interaction —— this enables methods of one instance (SELF) to utilise properties and behaviors of the passed object.

MATHS:
Combining Pythagorean Theorem with Cartesian Coordinate System: The hypot function calculates the distance between two points on a Cartesian plane (two dimensional space) by treating one point as the origin (0). 
By using self.__x - x and self.__y - y, we're effectively shifting the coordinate system's center to one of the points, simplifying the distance calculation to a single hypot call.

REFERENCES:
https://www.mathsisfun.com/data/cartesian-coordinates.html
'''