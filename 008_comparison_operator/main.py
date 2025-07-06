# Comparison operators are used to compare two values and return "True" or "False"!
# In simple words, they check whether one number is greater, smaller, equal, or not equal to another!

# Compare Race Speeds
# Speeds
your_speed = 10
uzair_speed = 8
faraz_speed = 10

# Compare
print(your_speed > uzair_speed)     # Are you faster than Uzair? → True
print(your_speed == faraz_speed)    # Do you and Faraz have the same speed? → True
print(uzair_speed < faraz_speed)    # Is Uzair slower than Faraz? → True

# Compare School Marks
your_marks = 85
faraz_marks = 78
uzair_marks = 85

print(your_marks > faraz_marks)        # Are your marks higher than Faraz's? → True
print(your_marks == uzair_marks)       # Are your marks equal to Uzair's? → True
print(faraz_marks != uzair_marks)      # Are Faraz and Uzair's marks different? → True

# Using comparison with an if statement
your_marks = 85

if your_marks > 80:
    print("Excellent! You scored very well!")
else:
    print("Work harder!")


# If a number divided by 2 gives remainder 0, it is Even
number = 7

if number % 2 == 0:
    print("This is an Even number!")
else:
    print("This is an Odd number!")
