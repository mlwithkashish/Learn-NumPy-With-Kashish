'''
 What Are Cumulative Operations?
Cumulative operations compute a running result over an array — such as cumulative sum or cumulative product.

They don’t reduce the array to a single number like aggregate functions — they return an array of the same shape showing step-by-step accumulation.


'''
import numpy as np

# 1D Cumulative Operations
a = np.array([1,2,3,4])
print("Original 1D:",a)
print("Cumulative Sum:",np.cumsum(a)) # 1 -- 1+2 -- 1+2+3 -- 1+2+3+4 --
print("Cumulative Product:",np.cumprod(a))
print("Cumulative Max:",np.maximum.accumulate(a)) 
print("Cumulative Min:",np.minimum.accumulate(a))
print()

# 2D Cumulative Operations
b = np.array([[1,2],
              [3,4]])
print("Original 2D:\n",b)
print("Cumsum axis=0 (column-wise):\n",np.cumsum(b,axis = 0))
print("Cumsum axis=1 (row-wise):\n",np.cumsum(b,axis=1))

# ============== NumPy Cumulative Operations Summary ===============
# ✅ np.cumsum()      → running sum
# ✅ np.cumprod()     → running product
# ✅ np.maximum.accumulate() → cumulative max
# ✅ np.minimum.accumulate() → cumulative min
# ✅ axis=0 → column-wise, axis=1 → row-wise for 2D arrays
# ==================================================================

