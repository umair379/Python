# In Python, Boolean values are written as "True" and "False" (First letter is capital).

x = True
y = False
print(x)  # Output: True
print(y)  # Output: False

# Boolean with Comparison Operators
a = 10
b = 5
print(a > b)   # Is 10 greater than 5? → True
print(a < b)   # Is 10 less than 5? → False
print(a == b)  # Is 10 equal to 5? → False
print(a != b)  # Is 10 not equal to 5? → True

# Boolean with if Statement
is_raining = True

if is_raining:
    print("Take an umbrella!")  # This runs when the condition is True
else:
    print("The weather is nice!")

# In Python, 0 (zero) is considered False, and all other numbers are True!
print(bool(0))     # False
print(bool(1))     # True
print(bool(-5))    # True
print(bool(100))   # True

# In Python, an empty string ("") is considered False, but any non-empty string is True!
print(bool(""))       # False (Empty string)
print(bool("Hello"))  # True (Because the string is not empty)
print(bool(" "))      # True (Even a space counts as True!)

# and, or, not Operators
x = True
y = False
print(x and y)  # False (Both must be True)
print(x or y)   # True (If at least one is True)
print(not x)    # False (not means to reverse the value)
