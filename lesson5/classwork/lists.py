colors = ["red", "green", "blue", "yellow"]  # Create a list

print(colors)  # Print the entire list

# Lists are 0 indexed
print("First color:", colors[0])  # Access items in a list by index
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])

# Error: list index out of range
# print(colors[10]) 

colors.append("orange")  # Adds an item to the end of the list
print("After append:", colors)

colors.insert(2, "purple")  # Insert an item at a specific index
print("After insert at index 2:", colors)

colors.remove("green")  # Remove the first occurrence of an item
print("After removing 'green':", colors)

# Error: removing item not in list
# colors.remove("pink")

popped_color = colors.pop()  # Remove and return the last item
print("Popped color:", popped_color)
print("After pop:", colors)

popped_color_at_index = colors.pop(1)  # Remove item at index 1
print("Popped color at index 1:", popped_color_at_index)
print("After pop at index 1:", colors)

index_of_blue = colors.index("blue")  # Find the index of an item
print("Index of 'blue':", index_of_blue)

# Error: finding index of item not in list
# colors.index("pink")

colors.append("blue")
blue_count = colors.count("blue")  # Count how many times an item appears
print("Count of 'blue':", blue_count)

colors.sort()  # Sort the list in alphabetical order
print("After sort:", colors)

colors.reverse()  # Reverse the order of the list
print("After reverse:", colors)
