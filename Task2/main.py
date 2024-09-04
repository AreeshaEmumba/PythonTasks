import math
import argparse

parser = argparse.ArgumentParser(description="Calculate distance from origin")
parser.add_argument("--Up", type=int, default=0, help="Distance moved up")
parser.add_argument("--Down", type=int, default=0, help="Distance moved down")
parser.add_argument("--Right", type=int, default=0, help="Distance moved right")
parser.add_argument("--Left", type=int, default=0, help="Distance moved left")

arguments = parser.parse_args()

def calculate_distance(u,d,r,l):
    vertical = u - d
    horizontal = r - l

    dist = math.sqrt(vertical**2 + horizontal**2)
    distance = round(dist)
    return distance

print("Distance from origin: ", calculate_distance(arguments.Up, arguments.Down, arguments.Right, arguments.Left))