import numpy as np

# Python List
py_list = [1, 2, 3]
# This will give an error: py_list + 10
# You have to use loop
list_result = [x + 10 for x in py_list]
print("Python List Result:", list_result)

# NumPy Array
np_array = np.array([1, 2, 3])
array_result = np_array + 10  # Vectorized addition
print("NumPy Array Result:", array_result)

'''
With lists, you must loop manually for element-wise operations.

With NumPy, operations like +, *, **, etc., work automatically on all elements.

NumPy is ideal for mathematical computing, data science, and machine learning.

'''