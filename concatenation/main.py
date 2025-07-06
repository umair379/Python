# do string ko  jodna
first_name = "Umair"
last_name = "Khan"

full_name = first_name + " " + last_name
print(full_name)


# multiple string ko jodna
greeting = "Hello"
name = "Umair"
message = "Welcome to Python!"

full_message = greeting + ", " + name + "! " + message
print(full_message)


# ghalti jo log karte hain string ko integer ke sath jodne ki
# age = 25
# message = "I am " + age + " years old."
# print(message)

# sahi tareeka ye hai k integer ko convert karlia jaaye string mai
age = 31
message = "I am " + str(age) + " years old."
print(message)


# Strings Concatenation Ka Dusra Tarika: f-strings
name = "Umair"
age = 31
message = f"My name is {name} and I am {age} years old."
print(message)




