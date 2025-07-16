
'''
What Are Rounding Functions?
NumPy provides functions to round, floor, ceil, and truncate numerical values — useful in both data preprocessing and mathematical modeling.

✅ Common Rounding Functions in NumPy
Function	Description	Example (x = 3.75)
np.round()	Rounds to nearest integer or decimal place	4.0
np.floor()	Rounds down to nearest whole number	3.0
np.ceil()	Rounds up to nearest whole number	4.0
np.trunc()	Truncates the decimal part (toward 0)	3.0
np.fix()	Same as truncation (toward 0)	3.0

'''

import numpy as np

# Original Array with positive and negative floats
arr = np.array([1.567 , 2.499 , 3.501 , -1.234 , -2.9 ])
print("Original Array:",arr)

# 01 Round to nearest integer (default decimals = 0)
rounded_nearest = np.round(arr)
print("np.round() to nearest:",rounded_nearest) # [2. 2. 4. -1. -3.]

# 02 Round to 2 decimal places
rounded_2_dec = np.round(arr,2)
print("np.round() to 2 decimals:",rounded_2_dec)

# 03 Floor --> round down to the nearest integer 
floored = np.floor(arr)
print("np.floor():",floored)  #[ 1. 2. 3. -2. -3.]

# 04 Ceil --> round up to nearest integer
ceiled = np.ceil(arr)
print("np.ceil():",ceiled) #[ 2. 3. 4. -1. -2.]

# 05 Truncate --> remove decimal part (towards zero)
truncated = np.trunc(arr)
print("np.trunc():",truncated) # [ 1. 2. 3. -1. -2.]

# 06 Fix -> same as trunc (towards zero)
fixed = np.fix(arr)
print("np.fix():",fixed) # [ 1. 2. 3. -1. -2.]

# ============== NumPy Rounding Functions Summary ===============
# ✅ np.round(arr, decimals=n) → Round to n decimal places
# ✅ np.floor(arr) → Round down to nearest whole number
# ✅ np.ceil(arr) → Round up to nearest whole number
# ✅ np.trunc(arr) / np.fix(arr) → Remove decimal part (toward 0)
# ➤ All methods preserve array shape and return float results
# ================================================================
