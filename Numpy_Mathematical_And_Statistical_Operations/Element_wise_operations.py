'''
What Are Element-wise Operations?
Element-wise operations apply mathematical operations to each element of an array independently.

These work between:

Arrays of the same shape

Or broadcast-compatible shapes
'''
import numpy as np

# 01 Element Wise Operations (same shape)
a = np.array([1,2,3])
b = np.array([10,20,30])

print("a:",a)
print("b:",b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("b / a:", b / a)
print("b % a:", b % a)
print("a ** 2:", a ** 2)
print("np.power(a, 3):", np.power(a, 3))
print()

# 02 Element Wise Functions
print("np.add(a,b):0",np.add(a,b))
print("np.subtract(b,a):",np.subtract(b,a))
print("np.multiply(a,b):",np.multiply(a,b))
print("np.divide(b,a):",np.divide(b,a))
print()

# 03 Element-wise with broadcasting
a2 = np.array([[1,2,3],
               [4,5,6]])

b2 = np.array([10,20,30])

print("a2:\n",a2)
print("b2:",b2)
print("a2 + b2:\n",a2+b2) # Broadcast row-wise

# ================= NumPy Element-wise Operations ==================
# ✅ Works on arrays of same shape or broadcast-compatible
# ➤ Arithmetic: +, -, *, /, %, ** 
# ➤ Functions: np.add(), np.subtract(), np.multiply(), np.divide()
# ✅ Broadcasting: smaller array is stretched to match shape
# Example: (2,3) + (3,) → valid
# Here, b is broadcast across rows of a
# ================================================================


