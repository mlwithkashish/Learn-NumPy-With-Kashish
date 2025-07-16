'''

Indexing means accessing specific elements of a NumPy array using their position (index).

'''
import numpy as np
# =============== 1D Array Indexing===================
arr1D=np.array([10,20,30,40,50])
print("1D Array: ",arr1D)
print("arr1D[0] --> First Element: ",arr1D[0])    #10
print("arr1D[2] --> Third Element: ",arr1D[2])    #30
print("arr1D[-1] --> Last Element: ",arr1D[-1])   #50
print()

# ================== 2D Array Indexing ==================
arr2D = np.array([[1,2],[3,4]])
print("2D Array:\n",arr2D)
print("arr2D[0][1] --> Row 0 , Col 1: ",arr2D[0][1]) #2
print("arr2D[1, 0] --> Row 1 , Col 0:",arr2D[1,0])  #3
print()

# =================== 3D Array Indexing =================
arr3D = np.array([
                  [[1,2],[3,4]], # depth 0
                  [[5,6],[7,8]]   # depth 1
                ]) 
print("3D Array:\n",arr3D)
print("arr3D[0, 1, 1] -->  Depth 0, Row 1, Col 1:", arr3D[0, 1, 1])  # 4
print("arr3D[1, 0, 0] -->  Depth 1, Row 0, Col 0:", arr3D[1, 0, 0])  # 5
print("arr3D[1, 1, 1] -->  Depth 1, Row 1, Col 1:", arr3D[1, 1, 1])  # 8

# ===================== Summary Tag =====================
# 1D: arr[index] → arr[0], arr[-1]
# 2D: arr[row, col] → arr[0, 1] = 2
# Both a[1][0] and a[1, 0] work, but a[1, 0] is preferred (faster & cleaner)
# 3D: arr[depth, row, col] → arr[1, 0, 0] = 5
# Always prefer arr[i, j] over arr[i][j] for multidimensional arrays
