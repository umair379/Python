# Logical operators check whether two or more conditions work together or not!

# Can You Take the Ride?
# Your Ticket & Weight
has_ticket = True
your_weight = 45

# Check the condition
if has_ticket and your_weight < 50:
    print("You can take the ride")
else:
    print("Sorry, you cannot take the ride")

# Can Bilal Take the Ride?
bilal_has_ticket = False
bilal_weight = 40

if bilal_has_ticket and bilal_weight < 50:
    print("Bilal can take the ride")
else:
    print("Bilal cannot take the ride")

# Can Zainab Take the Ride?
zainab_has_ticket = True
zainab_weight = 55

if zainab_has_ticket and zainab_weight < 50:
    print("Zainab can take the ride")
else:
    print("Zainab cannot take the ride")

# Can Anyone Get the Ride? (Using or Operator)
bilal_has_ticket = False
bilal_weight = 40

if bilal_has_ticket or bilal_weight < 50:
    print("Bilal can take the ride")
else:
    print("Bilal cannot take the ride")

# Using not Operator
bilal_has_ticket = False

if not bilal_has_ticket:
    print("Bilal does not have a ticket")
