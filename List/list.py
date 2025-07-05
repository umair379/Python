friends = ["Nimra", "Zainab", "Hamza", "Zubair", "Amna", "Bilal", "Sidra", "Atif"]

remove = friends.pop(2)  # the index we provide will be removed
# ["Nimra", "Zainab", "Zubair", "Amna", "Bilal", "Sidra", "Atif"] Hamza removed

friends.append("Umair")  # added at the end
# ["Nimra", "Zainab", "Zubair", "Amna", "Bilal", "Sidra", "Atif", "Umair"] Umair added

friends.insert(3, "Shahrukh")  # Shahrukh added at index 3
# ["Nimra", "Zainab", "Zubair", "Shahrukh", "Amna", "Bilal", "Sidra", "Atif", "Umair"]

friends.reverse()  # list starts from the last element
# ['Umair', 'Atif', 'Sidra', 'Bilal', 'Amna', 'Shahrukh', 'Zubair', 'Zainab', 'Nimra']

friends.remove("Atif")  # Atif removed
# ['Umair', 'Sidra', 'Bilal', 'Amna', 'Shahrukh', 'Zubair', 'Zainab', 'Nimra']

friends.sort()  # arranged in alphabetical order A to Z
# ['Amna', 'Bilal', 'Nimra', 'Shahrukh', 'Sidra', 'Umair', 'Zainab', 'Zubair']
print(friends)

friends.extend("Laraib")  # Laraib added at the end, broken into characters
# ['Amna', 'Bilal', 'Nimra', 'Shahrukh', 'Sidra', 'Umair', 'Zainab', 'Zubair', 'L', 'a', 'r', 'a', 'i', 'b']

copyList = friends.copy()  # created a duplicate of the list
# ['Amna', 'Bilal', 'Nimra', 'Shahrukh', 'Sidra', 'Umair', 'Zainab', 'Zubair', 'L', 'a', 'r', 'a', 'i', 'b']
copyList.pop(1)
# ['Amna', 'Nimra', 'Shahrukh', 'Sidra', 'Umair', 'Zainab', 'Zubair', 'L', 'a', 'r', 'a', 'i', 'b']

# print(friends.index("Umair")) # 5 will be printed because Umair is at index 5
print(friends.count("Amna"))  # 1 will be printed because Amna appears only once in the list
print(friends)
print(remove)
print(friends)
print(copyList)
print(friends)

for friend in friends:
    if len(friend) == 1:
        print(f"{friend} is not a friend")
    else:
        print(f"{friend} is a very good friend")

friends.clear()  # clears the list
print(friends)
