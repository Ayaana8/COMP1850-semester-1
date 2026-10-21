# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"


with open("../images/gradient.pgm","r") as infile:

    lineToListMapping = {}
    newLineToListMapping = {}
    maxGreyVal = 0

    data = infile.readlines()
    P2string = data[0]
    dimensions = data[1]
    maxGreyVal = int(data[2][0])

    data = [ line.strip().split(" ") for line in data[3:]]

    for i in range(len(data)):
        lineToListMapping[i] = data[i]

    for i in range(len(data)):
        newString = ""
        for j in range(len(lineToListMapping[i])):
            newString += (str((maxGreyVal)-int(lineToListMapping[i][j]))) + " "
        newLineToListMapping[i] = newString

with open("../images/new_gradient.pgm","w") as outfile:
    outfile.write(f"{P2string}\n{dimensions}\n{maxGreyVal}\n")
    for i in range(len(data)):
        outfile.write(f"{newLineToListMapping[i]}\n")


        
            