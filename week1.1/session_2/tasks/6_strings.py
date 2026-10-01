# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") 
print(f"Modified String 1: {user_string.lower()}") # converts each letter in the string to lowercase
print(f"Modified String 2: {user_string.upper()}") # converts each letter in the string to uppercase
print(f"Modified String 3: {user_string.strip()}") # removes all spaces at the beginning and end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces any occcurence of 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}") # converts the first letter of the string to uppercase
print(f"Modified String 6: {user_string[::-1]}") # reverses the string
print(f"Modified String 7: {user_string.title()}") # capitalises the first letter of each word
print(f"Modified String 8: {len(user_string)}") # outputs the length of the string
print(f"Modified String 9: {user_string.find('a')}") # finds the position of the first instance of the character 'a' and outputs -1 if there is no a
print(f"Modified String 10: {user_string.count('a')}") # counts the instances of the character 'a'
print(f"Modified String 11: {user_string.startswith('Hello')}") # outputs True if the string starts with Hello
print(f"Modified String 12: {user_string.endswith('!')}") # outputs True if the string ends with !
print(f"Modified String 13: {user_string.isalnum()}") # outputs True if the string contains only alphanumeric characters
print(f"Modified String 14: {user_string.isalpha()}") # outputs True if the string contains only alphabetic characters
print(f"Modified String 15: {user_string.isdigit()}") # outputs True if the string contains only digits 



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!