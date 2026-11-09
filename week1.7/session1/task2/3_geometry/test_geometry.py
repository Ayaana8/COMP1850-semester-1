# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5
    
    # complete the implementation for
    # testing distance_to()
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

import math

def test_circle_constructor():
    C = Circle(5)
    assert C.radius == 5
    assert C.centre.x == 0.0
    assert C.centre.y == 0.0

def test_circle_area():
    assert Circle(5).area() == 5*5*math.pi
    assert Circle(0.5).area() == 0.5*0.5*math.pi

def test_circle_perimeter():
    assert Circle(5).perimeter() == 10*math.pi
    assert Circle(0.5).perimeter() == 1*math.pi
