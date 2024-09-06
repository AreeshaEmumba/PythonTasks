import argparse
import json
import os
import random

# Function to estimate the value of π using the Monte Carlo method
def monte_carlo_pi(iterations):
    inside_circle = 0  # Counter for points inside the unit circle
    for _ in range(iterations):  # Loop over the number of iterations
        # Generate random point (x, y) where x and y are between 0 and 1
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1  # Increment count if inside the circle
    # Estimate π as 4 times the ratio of points inside the circle to total points
    return (inside_circle / iterations) * 4

# Function to load the number of iterations from a JSON file
def load_iterations_from_json():
    json_file = "iterations.json"  # Name of the JSON file
    if os.path.exists(json_file):  # Check if the JSON file exists
        with open(json_file, 'r') as file:  # Open the file for reading
            data = json.load(file)  # Parse the JSON data
            # Return the number of iterations specified in the JSON file, defaulting to 1000 if not found
            return data.get("iterations", 1000)
    else:
        print(f"Error: {json_file} not found.")  # Print error message if file is missing
        exit(1)  # Exit the program with an error code

# Main execution block
if __name__ == "__main__":
    # Create argument parser with a description
    parser = argparse.ArgumentParser(description="Monte Carlo simulation to estimate the value of pi.")
    # Define argument for specifying the number of iterations directly
    parser.add_argument("-i", "--iterations", type=int, help="Number of iterations for the simulation.")
    # Define argument for reading the number of iterations from a JSON file
    parser.add_argument("-j", "--json", action="store_true", help="Read number of iterations from Iterations.json.")
    
    args = parser.parse_args()  # Parse command-line arguments

    # Determine the source of the number of iterations
    if args.json:
        iterations = load_iterations_from_json()  # Load from JSON file if -j is used
    elif args.iterations:
        iterations = args.iterations  # Use value from -i flag if specified
    else:
        parser.print_help()  # Print help message if no valid arguments are provided
        exit(1)  # Exit the program with an error code

    # Perform Monte Carlo simulation to estimate π
    pi_estimate = monte_carlo_pi(iterations)
    # Print the estimated value of π and the number of iterations used
    print(f"Estimated value of pi after {iterations} iterations: {pi_estimate}")
