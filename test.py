# Importing NumPy, a powerful library for numerical computing in Python.
# It provides support for large, multi-dimensional arrays and matrices,
# along with a collection of mathematical functions to operate on them.
import numpy as np

# Create a 2D NumPy array with two rows and three columns.
# `np.array` is used to define the array structure and initialize its elements.
array = np.array([[1, 2, 3], [4, 5, 6]])

# Print the shape of the array.
# `array.shape` returns a tuple representing the dimensions of the array.
# For this array, it will return (2, 3), indicating 2 rows and 3 columns.
print("Array shape:", array.shape)