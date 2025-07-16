'''
What Are Aggregate Functions?
Aggregate functions reduce an array to a single value or summarize along an axis.

For example:

np.sum() gives the total

np.mean() gives the average

np.min(), np.max() for min/max

np.std() for standard deviation

np.var() for variance

'''
import numpy as np

# Sample Array
a = np.array([[1,2,3],
              [4,5,6]])

print("Original Array:\n",a)

# 01 Global Aggregates (entire array)
print("Sum:",np.sum(a))  #21
print("Mean:",np.mean(a)) #3.5
print("Min:",np.min(a)) # 1
print("Max:",np.max(a)) # 6
print("Std Dev:",np.std(a)) # standars deviation
print("Variance: ",np.var(a)) 
print("Product:", np.prod(a))           # 720
print("Cumulative Sum:", np.cumsum(a))  # [ 1  3  6 10 15 21]
print()

# 02 Aggregate By Axis 
print("Sum along axis=0 (columns):",np.sum(a,axis=0)) # [ 5 7 9 ]
print("Sum along axis=1 (rows):",np.sum(a,axis=1)) #[6 15]
print("Max Along axis = 0 (col):",np.max(a,axis=0)) # [4 5 6]
print("Min Along axis=1 (row):",np.min(a,axis=1)) # [1 4]


'''
# ============== NumPy Aggregate Functions Summary ==============
# ✅ Common Aggregates: sum, mean, min, max, std, var, prod, cumsum
# ✅ Axis:
#    ➤ axis=0 → column-wise
#    ➤ axis=1 → row-wise
# ✅ Example: np.sum(arr, axis=0) → sum of each column
# ============================================================== 
✅ Common Aggregate Functions
Function	Meaning
np.sum()	Sum of all elements
np.mean()	Mean (average)
np.min()	Minimum value
np.max()	Maximum value
np.std()	Standard deviation
np.var()	Variance
np.prod()	Product of all elements
np.cumsum()	Cumulative sum
'''
