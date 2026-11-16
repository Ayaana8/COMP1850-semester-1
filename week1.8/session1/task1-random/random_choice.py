import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

numOfNames = int(input("How many names? "))

randNames = []
randomNum = 0

for i in range(numOfNames):
    randomNum = random.randint(0,len(names))
    while names[randomNum] in randNames:
        randomNum = random.randint(0,len(names))
    randNames.append(names[randomNum])


# Display the chosen names, one per line
for i in randNames:
    print(i)
