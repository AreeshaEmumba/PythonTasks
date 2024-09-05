import math
import argparse

# Set up argument parsing  to allow user to input distance moved in each direction
parser = argparse.ArgumentParser(description="Calculate distance from origin")

# Adding arguments for each direction with default value 0
parser.add_argument("--Up", type=int, default=0, help="Distance moved up")
parser.add_argument("--Down", type=int, default=0, help="Distance moved down")
parser.add_argument("--Right", type=int, default=0, help="Distance moved right")
parser.add_argument("--Left", type=int, default=0, help="Distance moved left")

# Parse the arguments provided by the user
arguments = parser.parse_args()

# Input Handling : Validate inputs to ensure they are non-negative
if arguments.Up < 0 or arguments.Down < 0 or arguments.Right < 0 or arguments.Left < 0:
    # Print an error msg if any input is negative and exit the program
    print("\n Error! \n All inputs must be non-negative integers. \n Usage Emaple: \t --Up 10 --Down 20 --Right 0 --Left 3")
    exit(1) # Exit the program with an error code

# Function to calculate the distance from the origin after movements
def calculate_distance(up,down,right,left):
    
    # Calculate net vertical and horizontal movement
    vertical = up - down
    horizontal = right - left

    # Using Pythagoras Theorom to calculate the distance from the origin
    dist = math.sqrt(vertical**2 + horizontal**2)

    # Round the distance to the nearest integer
    distance = round(dist)
    return distance

# Print the calculated distance from the origin
print("Distance from origin: ", calculate_distance(arguments.Up, arguments.Down, arguments.Right, arguments.Left))
