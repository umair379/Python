# Simple f-string
name = "Umair"
age = 31
message = f"My name is {name} and I am {age} years old."
print(message)
# See the magic of f-strings? By placing variables inside {}, they are directly inserted into the string!


# Using expressions
a = 10
b = 5
result = f"Sum of {a} and {b} is {a + b}."
print(result)
# Python calculated {a + b} and automatically inserted the result into the string!


# Decimal formatting
price = 49.98765
formatted_price = f"The price is ${price:.2f}"
print(formatted_price)
# :.2f means "show only up to 2 decimal places".


# You can also use functions inside f-strings
def get_name():
    return "Nimra"
message = f"Hello, {get_name()}!"
print(message)


name = "Nimra"
age = 27

# Old method (concatenation)
message1 = "My name is " + name + " and I am " + str(age) + " years old."

# Old method (.format method)
message2 = "My name is {} and I am {} years old.".format(name, age)

# New method (f-string)
message3 = f"My name is {name} and I am {age} years old."

print(message1)
print(message2)
print(message3)

