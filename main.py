"""
This module demonstrates the use of matplotlib for creating various plots
and numpy for numerical operations.
"""

import matplotlib.pyplot as plt
import numpy as np


def get_data():
    """
    Function to generate sample data for plotting.
    Returns:
        tuple: (x_values, y_values) where both are lists of integers.
    """
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [10, 8, 6, 4, 2]
    return x_vals, y_vals


# Retrieve sample data
initial_x_vals, initial_y_vals = get_data()

# Plot 1: Simple Line Plot
plt.plot(initial_x_vals, initial_y_vals)
plt.title("Графік Х від Y")
plt.xlabel("X-ось")
plt.ylabel("Y-ось")
plt.show()


# Data for multiple plots
x_vals_multiple = [1, 2, 3, 4, 5]
y1_vals = [10, 8, 6, 4, 2]
y2_vals = [2, 4, 6, 8, 10]
y3_vals = [5, 5, 5, 5, 5]
y4_vals = [4, 5, 6, 7, 8]

# Plot 2: Multiple Lines on One Plot
plt.plot(x_vals_multiple, y1_vals, label='Line 1')
plt.plot(x_vals_multiple, y2_vals, label='Line 2')
plt.plot(x_vals_multiple, y3_vals, label='Line 3')
plt.plot(x_vals_multiple, y4_vals, label='Line 4')

plt.title("A Simple Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()  # Show legend for multiple lines
plt.show()


# Generate x values and compute y values for a function
x_vals_function = np.arange(0, 20, 0.2)
y_vals_function = x_vals_function**4

# Plot 3: Function Plot
plt.plot(x_vals_function, y_vals_function)
plt.title("Графік функції y = x^4")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
