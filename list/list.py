users = ["Jhon Doe", "Karim", "Rahim", "Jamal", "kamal", "Matin", "Halim"]
print(type(users))
print(users)


""" Access of List Item """
# Print First Item
print(users[0])

# Print Last Item
print(users[-1])

# Print Range Of Item
print(users[2:6])


""" Update List Item """
users[3] = "Sumon"
users[3:6] = ["Jashim", "Manna", "Salman Shah"]
print(users)

""" Manipulation List """

# Append() can add only an item end of the list
users.append("Kalam")
print(users)

# Insert() can add new item in any specific index but doeson't replace any item.
users.insert(1, "Asif")
print(users)

# extend() can add new list of item doesn't replace the item. and it add the items seperatedly instead the list
users.extend(["Neimar", "Messi"])
print(users)

# Add 1 or more list to the list
users = users + ["Christiano Ronaldo", "Karim Benzama"] + \
    ["Bill Gates", "Steve Jobs"]
print(users)

""" Remove and Delete """
# remove any item using del statement
del users[-1]
print(users)
del users[:2]
print(users)

# remove or delete the item using remove() method
users.remove("Karim Benzama")
print(users)
# remove the last item using pop() method
users.pop()
print(users)
# remove the last item using pop() method
users.pop(3)
print(users)

""" List size """

# Length of the lists
print(len(users))

# count any item in the list
print(users.count("Messi"))

users.reverse()
print(users)

# Ascending Order
users.sort()
print(users)

peoples = users.copy()

users.clear()
print(users)
print(peoples)