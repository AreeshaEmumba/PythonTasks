import math

print("Up : ")
up = int(input())
print("Down : ")
down = int(input())
print("Right : ")
right = int(input())
print("Left : ")
left = int(input())

vertical = up - down
horizontal = right - left

dist = math.sqrt(vertical**2 + horizontal**2)
distance = round(dist)

print("Distance from origin: ", distance)