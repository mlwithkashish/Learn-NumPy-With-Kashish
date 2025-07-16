'''
What is Broadcasting in NumPy?
Broadcasting is a powerful feature in NumPy that allows arithmetic operations between arrays of different shapes.

 If shapes are compatible, NumPy automatically "stretches" the smaller array across the larger one without copying data.
Behind the Scenes:
a.shape = (2, 3)
b.shape = (3,)

➡️ NumPy broadcasts b row-wise (2 times) to match shape (2, 3):

text
Copy
Edit
[[10, 20, 30],
 [10, 20, 30]]
Then element-wise addition happens.


'''

import numpy as np

# Example 01 : 2D + 1D

a = np.array([[1,2,3],
              [4,5,6]])
b = np.array([10,20,30])
print("a:\n",a)
print("b:\n",b)
print("a + b (broadcasted row-wise):\n", a+b)
print()

# Example 02 : Broadcasting  A Column Vector
a = np.array([[1],[2],[3]]) # Shape: (3,1)
b = np.array([10 , 20 , 30]) # Shape: (3,)
print("a:\n",a)
print("b:",b)
try:
    print("a + b:\n", a + b)    # This will raise an error due to shape mismatch
except ValueError as e:
    print("Error:", e)

# Example 03: Compatible shapes
a = np.array([[1], [2], [3]])   # Shape: (3,1)
b = np.array([10, 20, 30, 40])  # Shape: (4,)
print("Broadcasting to (3,4):\n", a + b)

# ================= NumPy Broadcasting Summary =================
# ✅ Broadcasting = NumPy's way of auto-expanding arrays to match shapes
# ✅ Works when: dimensions are equal OR one is 1
# ✅ Common use: 2D + 1D → row-wise or column-wise operations
# Example: (2,3) + (3,) → broadcast (3,) to (2,3)
# Example: (3,1) + (4,) → result shape (3,4)
# ==============================================================


