fruits = ["apple","banana","cherry"]

# Find if apple is in the list
if "apple" in fruits:
  print("found apple.")
else:
  print("apple not found")

found = False
index = -1

for i in range(len(fruits)): # Looping through the list
  if fruits[i] == "apple":　# Checking if current item is apple
    found = True # Mark as found
    index = i # Store the index where we found an apple
    break # Exit the loop since we found apple

if found == True:
  print("found apple.")
else:
  print("no apple in list.")
