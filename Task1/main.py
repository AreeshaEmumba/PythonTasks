"""
This script finds all numbers between 2000 and 3200 (inclusive) that are divisible by 7 but not multiples of 5.
The resulting numbers are printed in a comma-separated sequence on a single line.
"""

# List to store the numbers in
num = []

# Iterate through the specified range
for i in range(2000,3201):
    # If the number is divisible by 7 and not a multiple of 5
    if i%7 == 0 and i%5 != 0:
        # Append each number to the list
        num.append(i)

# Print the list in a single line, with each element separated by a comma
print(*num, sep=", ")