import numpy as np

# 1
# Create a one-dimensional NumPy array
arr_1d = np.array([1, 2, 3, 4, 5])
print("One-dimensional array:\n", arr_1d)

# Create a two-dimensional NumPy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nTwo-dimensional array:\n", arr_2d)

#2
# Operations on one-dimensional array
print("Addition:\n", arr_1d + 2)
print("Subtraction:\n", arr_1d - 2)
print("Multiplication:\n", arr_1d * 2)
print("Division:\n", arr_1d / 2)

# Element-wise multiplication of two-dimensional arrays
arr_2d_2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("\nElement-wise multiplication:\n", arr_2d * arr_2d_2)

#3
# Calculations on one-dimensional array
print("Sum:", np.sum(arr_1d))
print("Mean:", np.mean(arr_1d))
print("Standard Deviation:", np.std(arr_1d))

# Sum of all elements in two-dimensional array
print("\nSum of two-dimensional array:", np.sum(arr_2d))

#4
# Reshape two-dimensional array
reshaped_arr = arr_2d.reshape(1, 9)
print("Reshaped array:\n", reshaped_arr)

# Slice to extract the second row
second_row = arr_2d[1, :]
print("\nSecond row:\n", second_row)
