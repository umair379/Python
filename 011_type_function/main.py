# The type() function returns the data type of any value or variable.
# It tells which category the value belongs to, such as:

# Checking basic data types
print(type(10))        # Integer
print(type(3.14))      # Float
print(type("Hello"))   # String
print(type([1, 2, 3])) # List
print(type((4, 5, 6))) # Tuple
print(type({"name": "Umair", "age": 31}))  # Dictionary

# Checking the type of a variable
x = 50
y = "Python"
z = 3.5

print(type(x))  # Integer
print(type(y))  # String
print(type(z))  # Float

# Type of a custom class
class Car:
    pass

c = Car()
print(type(c))  # <class '__main__.Car'>

# Using isinstance(), it checks whether a value is of a specific type like int or float
x = 100
print(isinstance(x, int))   # True
print(isinstance(x, float)) # False
