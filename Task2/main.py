import math

print("Up : ")
up = int(input())
print("Down : ")
down = int(input())
print("Right : ")
right = int(input())
print("Left : ")
left = int(input())

def calculate_distance(u,d,r,l):
    vertical = u - d
    horizontal = r - l

    dist = math.sqrt(vertical**2 + horizontal**2)
    distance = round(dist)
    return distance

print("Distance from origin: ", calculate_distance(up,down,right,left))
