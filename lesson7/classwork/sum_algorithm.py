numbers = [5, -8, 35, -3, 6, 2]

toatl = sum(numbers) # Shortcut to find sum
print("The sum is:", total)

print("Our algorithm:")

toatl2 = 0
for i in range(len(numbers)): # Go through each index in the list
  item = numbers[i] # Get the number at the current index
  toatal2 = toatl2 + item  # Add the current number to the total
print("The sum is:", total2)

# Find the sum of only the positive numbers.

total3 = 0
for i in range(len(numbers)): # Go through each index in the list
  item = numbers[i] # Get the number at the current index
  if item > 0: # Check if the current number is positive
    total3 = total3 + item # Add the current number to the running total if it is positive
print("The sum of only the positive numbers is:", total3)
