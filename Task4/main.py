import argparse
import json
import os
import random

def monte_carlo_pi(iterations):
    inside_circle = 0
    for _ in range(iterations):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / iterations) * 4

def load_iterations_from_json():
    json_file = "iterations.json"
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data.get("iterations", 1000)
    else:
        print(f"Error: {json_file} not found.")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monte Carlo simulation to estimate the value of pi.")
    parser.add_argument("-i", "--iterations", type=int, help="Number of iterations for the simulation.")
    parser.add_argument("-j", "--json", action="store_true", help="Read number of iterations from Iterations.json.")
    
    args = parser.parse_args()

    if args.json:
        iterations = load_iterations_from_json()
    elif args.iterations:
        iterations = args.iterations
    else:
        parser.print_help()
        exit(1)

    pi_estimate = monte_carlo_pi(iterations)
    print(f"Estimated value of pi after {iterations} iterations: {pi_estimate}")

