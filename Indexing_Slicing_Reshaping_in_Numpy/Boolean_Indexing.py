'''
What is Boolean Indexing in NumPy?
Boolean Indexing = Filtering elements from an array based on a condition.

It works by:

Applying a condition to the array → returns a Boolean array (True/False)

Using that Boolean array to extract elements where the condition is True
Use &, |, ~ for:

& → AND

| → OR

~ → NOT

 Always wrap conditions in parentheses when combining!


'''
import numpy as np

# 1D Example
a1D = np.array([1,2,3,4,5])
print("1D Array:",a1D)
print("Condition (a1D > 3): ",a1D > 3) # [False False False  True  True]
print("Filtered (a1D[a1D > 3]): ",a1D[a1D > 3]) # [4 5]
print()
# 2D Example
a2D = np.array([[1, 2, 3],
                [4, 5, 6]])
print("2D Array:\n", a2D)
print("Condition (a2D > 3):\n", a2D > 3)
print("Filtered (a2D[a2D > 3]):", a2D[a2D > 3])  # [4 5 6]
print()

# Multiple Conditions
a = np.array([10, 15, 20, 25, 30])
print("Original:", a)
print("a[(a >= 15) & (a <= 25)]:", a[(a >= 15) & (a <= 25)])  # [15 20 25]
print("a[a != 20]:", a[a != 20])  # [10 15 25 30]

# ====================== NumPy Boolean Indexing Summary ========================
#  Boolean Indexing = filtering based on condition → arr[condition]
#  Condition returns boolean array → used for selection
#  Combine conditions using: (&) AND, (|) OR, (~) NOT
#      Example: arr[(arr > 10) & (arr < 20)]
#  Works on 1D, 2D, 3D arrays → returns filtered 1D output
# ============================================================================== 
