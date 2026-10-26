# Week 1.5, Session 1: Task 3

import math
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



# Finally, add code here to demonstrate use of Point

p = Point(2,4)
q = Point(3,5)
print(p.distance())
print(p.distance_to(q))
