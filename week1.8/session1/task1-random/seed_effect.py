# See README.md for instructions on what to do this program

import random

random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

#The seed provides the input to the function that generates the numbers
#If the seed is the same, the generated numbers will be the same
#If there is no seed, the generated numbers will be different
