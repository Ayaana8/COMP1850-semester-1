# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point
from geometry import Circle

P = Point(2,5)
C = Circle(5,P)

SecondPoint = Point(10,20)
print(SecondPoint in C)

SecondPoint = Point(3,4)
print(SecondPoint in C)
