# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)
# tomato because it occurs in both lists

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)
# tomato is only displayed once

# Add an item to fruit
fruit.add("pear")
print(fruit)
# Remove an item from vegetables
vegetables.remove("leek")
print(vegetables)
# Find and display symmetric difference of the two sets
symDiff = fruit.symmetric_difference(vegetables)
print(symDiff)