# Week 1.3, Session 1: Task 5a

course = "computer science"

courseList = []

for ch in course:
	courseList.append(ch)

print(courseList)

courseList.sort()

print(courseList)

# Implementing using range

for ch in range(len(course)):
	courseList.append(course[ch])



# create a list data structure of the characters from the course string
# sort the list into alphabetical order