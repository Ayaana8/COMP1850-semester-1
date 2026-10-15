# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content


with open("../images/gradient.pgm","r") as infile:
        lines = infile.readlines()
        dimensions = lines[1].split()
        maxGreyVal = lines[2]
        width = dimensions[0]
        height = dimensions[1]

        for line in infile:
            lineList = line.split()
            for i in range(len(lineList)):
                  if i > maxGreyVal or i < 0:
                        print("Invalid pixel values")


# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value