# Joining two strings
first_name = "Umair"
last_name = "Khan"
full_name = first_name + " " + last_name
print(full_name)

# Joining multiple strings
greeting = "Hello"
name = "Umair"
message = "Welcome to Python!"

full_message = greeting + ", " + name + "! " + message
print(full_message)

# Common mistake: trying to join a string with an integer
# age = 25
# message = "I am " + age + " years old."
# print(message)

# Correct way: convert the integer to a string first
age = 31
message = "I am " + str(age) + " years old."
print(message)

# Another way of string concatenation: f-strings
name = "Umair"
age = 31
message = f"My name is {name} and I am {age} years old."
print(message)
