# Using strings
name = "Umair"
city = "Karachi"
message = "I love coding!"

print(name)
print(city)
print(message)

# Using integers
age = 31
year = 2025
score = 100

print(age)
print(year)
print(score)

age = 31  # Integer
year = 2025  # Integer

# Converting integer to string for concatenation
print("My age is " + str(age) + " and the year is " + str(year))

num1 = "10"  # This is a string
num2 = "5"   # This is also a string

# Mistake: If we directly use +, it will just join the strings, not add them!
print(num1 + num2)  # Output: "105" (wrong!)

# Correct way: First convert the strings to integers
total = int(num1) + int(num2)
print(total)  # Output: 15
