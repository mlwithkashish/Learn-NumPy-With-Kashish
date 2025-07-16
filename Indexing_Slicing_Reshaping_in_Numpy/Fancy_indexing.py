'''
What is Fancy Indexing?
Fancy Indexing lets you select elements from a NumPy array by passing a list or array of indices.

Works for 1D, 2D, 3D arrays

Supports advanced row/column selection

Output is not a view but a copy of the data


'''
import numpy as np

# 01 Fancy Indexing in 1D
a1D = np.array([10,20,30,40,50])
indices_1D = [ 0 , 2 , 4]
print("1D Array:",a1D)
print("Fancy Indexed (a1D[0,2,4]):",a1D[indices_1D]) # [ 10 30 50 ]
print()

# 02 Fancy Indexing in 2D (selecting rows)
a2D = np.array([[10,11],
                [20,21],
                [30,31]])
row_ids = [0,2]
print("2D Array:\n",a2D)
print("Selected rows a2D[0,2]:\n",a2D[row_ids])
print()

# 03 Fancy Indexing : Selecting Specific Elements
a = np.array([[10,11,12],
              [20,21,22],
              [30,31,32]])
row_idx = np.array([0,1,2])
col_idx = np.array([2,1,0])
print("2D Array:\n",a)
print("a[row_idx, col_idx] = [a[0,2], a[1,1], a[2,0]]:", a[row_idx, col_idx])  # [12 21 30]


# ====================== NumPy Fancy Indexing Summary ==========================
#  Use index arrays/lists to access multiple specific elements
#  a[[0, 2, 4]] → selects multiple non-consecutive items from 1D array
#  a[[0, 2], :] → selects rows 0 and 2 from 2D array
#  a[rows, cols] → selects elements at each (row[i], col[i]) pair
#      Example: a[[0,1,2], [2,1,0]] → [a[0,2], a[1,1], a[2,0]]
# How It Works:
# It grabs:

# a[0,2] = 12

# a[1,1] = 21

# a[2,0] = 30
'''
✅ Summary:
Expression	Meaning
a2D[[0, 2]]	Select rows 0 and 2 (full rows)
a2D[0, 1]	Select element at row 0, col 1
a2D[:, 1]	Select entire 2nd column
a2D[[0, 2], :]	Same as selecting rows 0 and 2
'''
# ============================================================================
