'''
Slicing means selecting a portion (range) of an array using this syntax:

array[start : stop : step]
start: index where slice starts (inclusive)

stop: index where slice ends (exclusive)

step: optional; default is 1

It works on 1D, 2D, 3D arrays, etc.

'''
import numpy as np

# ========= 1D Array Slicing ============
a1D=np.array([0,10,20,30,40,50])
print("1D Array: " ,a1D)
print("a1D[1:4] --> index 1 to 3 elements: ",a1D[1:4])  # [10 20 30]
print("a1D[:3] --> first 3 elements: ",a1D[:3]) #[ 0 10 20]
print("a1D[::2] --> Every 2nd Elements: ",a1D[::2]) #[ 0 20 40]
print("a1D[::-1] --> Reversed Array: ",a1D[::-1]) #[50 40 30 20 10 0]
print()

# ========== 2D Array Slicing ===========
a2D = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print("2D Array:\n",a2D)

# Slice rows 0 and 1 , columns 1 and 2
print("a2D[0:2 , 1:3] --> rows 0-1 , cols 1-2:\n",a2D[0:2 , 1:3]) #[[2 3] ,[5 6]]
print
# Entire first row
print("a2D[0, :] --> first row:", a2D[0, :])                    # [1 2 3]
print()
# Entire second column
print("a2D[:, 1] --> second column:", a2D[:, 1])                # [2 5 8]
print()
# Bottom-right 2x2 block
print("a2D[1:, 1:] --> bottom-right 2x2:\n", a2D[1:, 1:])        # [[5 6], [8 9]]
print()
# Reverse rows
print("a2D[::-1] --> reverse rows:\n", a2D[::-1])
print()
# Reverse columns
print("a2D[:, ::-1] --> reverse columns:\n", a2D[:, ::-1])

# ======================== NumPy Slicing Summary =========================
#  1D Slicing: arr[start:stop:step]
#  2D Slicing: arr[row_start:row_end, col_start:col_end]
#      arr[0, :]     → entire first row
#      arr[:, 1]     → entire second column
#      arr[::-1]     → reverse rows
#      arr[:, ::-1]  → reverse columns
# =========================================================================





