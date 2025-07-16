import numpy as np

# Original Array
arr=np.array([1,5,10,15,20])
print("Original:",arr)

# Clipping
'''
 np.clip()
 What It Does:
Limits values in an array to a specified range — anything below min is set to min, and anything above max is set to max.

 Syntax: np.clip(array, min_val, max_val)
 
 '''
clipped = np.clip(arr , 5 , 15)
print(" Clipped (5,15):",clipped) # [ 5 5 10 15 15]

# Where with 3 values (condition , true_val, false_val)
'''
2. np.where()
 What It Does:
Performs element-wise condition-based selection:

 Syntax:  np.where(condition, value_if_true, value_if_false) 

 If you use only a condition, it returns the indices where the condition is True:


'''

labeled = np.where(arr > 10, "High" , "Low")
print("Labels based on > 10:",labeled) #['Low' 'Low' 'Low' 'High' 'High']

# Where with only condition --> returns indices
indices = np.where(arr < 10)
print("Indices where arr < 10:",indices) # (array([0,1]),)

# Using where with arithmetic 
bonus = np.where(arr > 15 , arr* 1.1 , arr)
print("Bonus Applied if > 15:",bonus) #[ 1.  5. 10. 15. 22.]

# ============== NumPy Clipping & Where ===================
#  np.clip(arr, min, max) → clamps values between bounds
#  np.where(condition, x, y) → if condition True → x, else y
#  np.where(condition) → returns indices where condition is True
#  Used for: filtering, labeling, replacing, bounding
# ==========================================================

