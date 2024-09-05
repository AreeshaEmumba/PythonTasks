
def square(lst):
    return [x**2 for x in lst]

def cube(lst):
    return [x**3 for x in lst]

X = [1,2,3,4,5,6,7,8,9,10]

squared_values = square(X)
cubed_values = cube(X)

print (squared_values, "\n", cubed_values)