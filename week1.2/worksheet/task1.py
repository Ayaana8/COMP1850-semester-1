# Worksheet 1.2: Task 1 Solution

import sys

try:

    grade = int(input("Enter a grade in the range 0 to 100: "))

    if grade >=70 and grade <=100:
        print(f"{grade} is a Distinction")
    elif grade >=40 and grade <=69:
        print(f"{grade} is a Pass") 
    elif grade >=0 and grade <=39:
        print(f"{grade} is a Fail") 
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
     sys.exit("Error: Grade must be an integer between 0 and 100")

    