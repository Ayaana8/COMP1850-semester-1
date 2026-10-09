# Worksheet 1.2: Task 2 Solution

from util import read_numbers
import sys

numbers = read_numbers()

if numbers:
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / len(numbers)
    median = 0
    orderedNum = sorted(numbers)

    if len(numbers) % 2 != 0:
        median = orderedNum[(len(numbers) // 2)]
    else:
        median = ((orderedNum[len(numbers)//2 - 1]) + (orderedNum[len(numbers)//2])) / 2

    print(f"Maximum = {maximum}")
    print(f"Minimum = {minimum}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")
    

else:
    sys.exit("Error: no numbers provided")

