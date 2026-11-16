import random

# Get user to input how many random numbers they want
numOfRand = int(input("How many random numbers do you want? "))

# Generate this many random numbers
randNums =[]
for i in range(numOfRand):
    randNums.append(random.randint(1,100))

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt","w") as outfile:
    for i in randNums:
        outfile.write(f"{i}\n")

