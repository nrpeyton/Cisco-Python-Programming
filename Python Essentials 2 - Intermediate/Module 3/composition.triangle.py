'''                                             3.4.1.15 LAB: Triangle

DIFFICULTY: Medium
TIME: 30-60 minutes

OBJECTIVES:
-Master class definition from scratch.
-Understand and implement composition.

SCENARIO:
Build a Triangle class that embeds three Point class objects to define a triangle.

FEATURES:
-Constructor accepts three Point objects.
-Points stored as a private list within the object.
-Provides a 'perimeter()' method to calculate the triangle's perimeter based on the three points.

TEST DATA:
Expected output: 3.414213562373095

'''



import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x  # Initialise x-coordinate of this Point object
        self.__y = y

    def getx(self):
        return self.__x  # Retrieve x-coordinate of this Point object

    def gety(self):
        return self.__y  # Retrieve y-coordinate of this Point object

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)  # Compute distance from this Point object to given x, y coordinates

    def distance_from_point(self, point):
        # Compute distance from this Point object to another Point object by using their x, y coordinates
        return self.distance_from_xy(point.getx(), point.gety())  


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1 # Initialise vertices; remember each vertice is a Point object.
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3

    def perimeter(self):                                         # Compute distance for each triangle side:
        a = self.__vertice1.distance_from_point(self.__vertice2) # Invoke distance_from_point on vertice1 (Point object) to calculate the distance to vertice2. 
        b = self.__vertice2.distance_from_point(self.__vertice3) # ...
        c = self.__vertice3.distance_from_point(self.__vertice1) # ...
        
        return a + b + c
    


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1)) # Creating a Triangle class object initialises its vertices with Point objects, each holding x, y coordinates.
print(triangle.perimeter())



# NOTES:
# Completed this without any help or notes, but a thorough understanding of a previous lab definitely helped:  object_properties.points_on_a_plane.py