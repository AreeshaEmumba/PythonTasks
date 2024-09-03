"""
This script finds all numbers between 2000 and 3200 (inclusive) that are divisible by 7 but not multiples of 5.
The resulting numbers are printed in a comma-separated sequence on a single line.
"""
# Iterate through the specified range
for i in range(2000,3200):
    # If the number is divisible by 7 and not a multiple of 5
    if i%7 == 0 and i%5 != 0:
        # Print the numbers in one line separated by a comma
        print(i, end=", ")