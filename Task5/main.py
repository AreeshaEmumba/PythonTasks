import matplotlib.pyplot as plt

def square(lst):
    return [x**2 for x in lst]

def cube(lst):
    return [x**3 for x in lst]

X = [1,2,3,4,5,6,7,8,9,10]

squared_values = square(X)
cubed_values = cube(X)

print (squared_values, "\n", cubed_values)

plt.figure(figsize=(10,5))

plt.subplot(1,1,1)
plt.plot(X, squared_values, marker = 'o', color = 'blue' , label = 'x^2')
plt.title("Square of first 10 natural numbers")
plt.xlabel("Natural Numbers")
plt.ylabel("Squared Values")

plt.show()