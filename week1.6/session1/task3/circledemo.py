# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from point import Point
from shapes import Shape
from shapes import Circle

P= Point(2,3)
C = Circle(4,P)
print(C)
print(C.area())
print(C.perimeter())
newP = Point(2,5)
C.set_position(newP)
C.set_colour("green")
print(C)


