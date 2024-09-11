import math

# Function to calculate the distance from the origin after movements
def calculate_distance(up, down, right, left):
    # Calculate net vertical and horizontal movement
    vertical = up - down
    horizontal = right - left

    # Using Pythagoras Theorem to calculate the distance from the origin
    dist = math.sqrt(vertical**2 + horizontal**2)

    # Round the distance to the nearest integer
    distance = round(dist)
    return distance

# Function to take user inputs manually and validate them
def take_input():
    while True:
        try:
            # Take input from user for each direction and ensure it's non-negative
            up = float(input("Enter distance moved UP (non-negative): "))
            down = float(input("Enter distance moved DOWN (non-negative): "))
            right = float(input("Enter distance moved RIGHT (non-negative): "))
            left = float(input("Enter distance moved LEFT (non-negative): "))

            # Round the inputs
            up, down, right, left = round(up), round(down), round(right), round(left)

            # Check for non-negative values
            if up < 0 or down < 0 or right < 0 or left < 0:
                raise ValueError("All inputs must be non-negative.")

            return up, down, right, left  # Return the valid inputs
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter valid inputs.\n")

# Main loop to keep running the program until the user decides to quit
while True:
    # Get the user input
    up, down, right, left = take_input()

    # Calculate and print the distance
    distance = calculate_distance(up, down, right, left)
    print("\nDistance from origin:", distance)

    # Ask if the user wants to run the program again
    retry = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
    if retry != 'yes':
        print("\nExiting the program.")
        break
