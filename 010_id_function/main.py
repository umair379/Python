# The id() function returns the unique memory address of any variable or object.


x = 10
print(id(x))  # Example: 140731843213456


# Checking the address of two variables with the same value
a = 100
b = 100
print(id(a))  # Example: 140731209371656
print(id(b))  # Example: 140731209371656
# Both variables (a and b) have the same id!
# This is because Python uses memory optimization and stores small integers (from −5 to 256) at the same address.


# If the value is large, Python allocates a new memory address.
x = 1000
y = 1000
print(id(x))  # Example: 140731843214400
print(id(y))  # Example: 140731843214720


# Testing id() with a list
numbers = [1, 2, 3]
print(id(numbers))  # Print ID before modification
numbers.append(4)
print(id(numbers))  # Print ID after modification


# id() with strings
s = "hello"
print(id(s))  # 2107707098096


s = s + " world"
print(id(s))  # 2107707078704
