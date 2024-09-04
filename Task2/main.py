import math
import argparse

parser = argparse.ArgumentParser(description="Calculate distance from origin")
parser.add_argument("--Up", type=int, default=0, help="Distance moved up")
parser.add_argument("--Down", type=int, default=0, help="Distance moved down")
parser.add_argument("--Right", type=int, default=0, help="Distance moved right")
parser.add_argument("--Left", type=int, default=0, help="Distance moved left")

arguments = parser.parse_args()

if arguments.Up < 0 or arguments.Down < 0 or arguments.Right < 0 or arguments.Left < 0:
    print("\n Error! \n All inputs must be non-negative integers. \n Usage Emaple: \t --Up 10 --Down 20 --Right 0 --Left 3")
    exit(1)

def calculate_distance(up,down,right,left):
    vertical = up - down
    horizontal = right - left

    dist = math.sqrt(vertical**2 + horizontal**2)
    distance = round(dist)
    return distance

print("Distance from origin: ", calculate_distance(arguments.Up, arguments.Down, arguments.Right, arguments.Left))