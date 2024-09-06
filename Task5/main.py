import matplotlib.pyplot as plt  # Import the matplotlib library for plotting

def square(lst):
    """Returns a list of squares of the given numbers."""
    return [x**2 for x in lst]  # List comprehension to square each element in lst

def cube(lst):
    """Returns a list of cubes of the given numbers."""
    return [x**3 for x in lst]  # List comprehension to cube each element in lst

# Define a list of numbers from 1 to 10
X = [1,2,3,4,5,6,7,8,9,10]

# Compute the squared and cubed values for the list X
squared_values = square(X)
cubed_values = cube(X)

# Print the squared and cubed values to the console
print(squared_values, "\n", cubed_values)

# Create a new figure with a specific size (10 inches by 5 inches)
plt.figure(figsize=(10,5))

# Create the first subplot (1 row, 2 columns, 1st subplot)
plt.subplot(1,2,1)
plt.plot(X, squared_values, marker='o', color='blue', label='x^2')  # Plot squared values with blue markers
plt.title("Square of first 10 natural numbers")  # Title for the first subplot
plt.xlabel("Natural Numbers")  # Label for the x-axis
plt.ylabel("Squared Values")  # Label for the y-axis

# Create the second subplot (1 row, 2 columns, 2nd subplot)
plt.subplot(1,2,2)
plt.plot(X, cubed_values, marker='o', color='red', label='x^3')  # Plot cubed values with red markers
plt.title("Cube of first 10 Natural Numbers")  # Title for the second subplot
plt.xlabel("Natural Numbers")  # Label for the x-axis
plt.ylabel("Cubed Values")  # Label for the y-axis

plt.tight_layout()  # Adjust layout to prevent overlap of subplots
plt.show()  # Display the figure with both subplots
