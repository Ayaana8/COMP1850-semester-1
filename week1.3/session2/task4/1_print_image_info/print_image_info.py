# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)

heightCount = 0
maxGreyValue= 0

with open("../images/gradient.pgm","r") as infile:
    for i in range(3):
        next(infile)
    for line in infile:
        lineList = line.split()
        width = len(lineList)
        heightCount +=1
        maxGreyValue = max(lineList)

print(f"Dimensions: {width} x {heightCount}")
print(f"Maximum grey value {maxGreyValue}")

