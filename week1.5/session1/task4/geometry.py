# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
# Week 1.5, Session 1: Task 3
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a point given x and y coordinates
        """
        self.x = x_coordinate
        self.y = y_coordinate
    # Add distance() method here
    def distance(self):
        """
        Returns the distance from this point to the origin
        """
        return math.hypot(self.x,self.y)
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self,another_point):
        """
        Returns the distance from this point to another point
        """
        return math.sqrt((self.x - another_point.x) * (self.x - another_point.x) + (self.y - another_point.y) * (self.y - another_point.y))

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        return math.pi * self.radius *self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
