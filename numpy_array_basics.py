#SINGH KASHISH
#13-07-2025 11:25

''' 
What is an ndarray?
ndarray stands for n-dimensional array.

It is the core data structure of NumPy.

It can represent:

0D array → scalar (e.g. np.array(5))

1D array → vector (e.g. np.array([1, 2, 3]))

2D array → matrix (e.g. np.array([[1, 2], [3, 4]]))

.shape tells the size in each dimension

.ndim tells how many dimensions the array has

.dtype tells the type of the array elements

.itemsize	   Memory (in bytes) of a single element

.nbytes	      Total memory consumed by the array = itemsize × number of elements

'''
import numpy as np

# 0-D Array (Scalar)
arr0 = np.array(5)
print("0-D Array (Scalar): ",arr0)
print("Shape: ",arr0.shape)
print("Dimensions: ",arr0.ndim)
print("Data Type: ",arr0.dtype)
print("Item Size:", arr0.itemsize, "bytes")
print("Total Bytes:", arr0.nbytes, "bytes")
print()

# 1-D Array (Vector)
arr1 = np.array([1,2,3,4])
print("1-D Array (Vector):",arr1)
print("Shape: ",arr1.shape)
print("Dimensions: ",arr1.ndim)
print("Data Type: ",arr1.dtype)
print("Item Size:", arr1.itemsize, "bytes")
print("Total Bytes:", arr1.nbytes, "bytes")
print()

# 2-D Array (Matrix)
arr2 = np.array([[1,2],[3,4]])
print("2D Array (Matrix):\n",arr2)
print("Shape: ",arr2.shape)
print("Dimensions: ",arr2.ndim)
print("Data Type: ",arr2.dtype)
print("Item Size:", arr2.itemsize, "bytes")
print("Total Bytes:", arr2.nbytes, "bytes")
print()

# 3-D Array (Tensor)
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array (Tensor):\n", arr3)
print("Shape:", arr3.shape)
print("Dimensions:", arr3.ndim)
print("Data Type:", arr3.dtype)
print("Item Size:", arr3.itemsize, "bytes")
print("Total Bytes:", arr3.nbytes, "bytes")
'''
O/P:
0-D Array (Scalar):  5
Shape:  ()
Dimensions:  0
Data Type:  int64
Item Size: 8 bytes
Total Bytes: 8 bytes

1-D Array (Vector): [1 2 3 4]
Shape:  (4,)
Dimensions:  1
Data Type:  int64
Item Size: 8 bytes
Total Bytes: 32 bytes

2D Array (Matrix):
 [[1 2]
 [3 4]]
Shape:  (2, 2)
Dimensions:  2
Data Type:  int64
Item Size: 8 bytes
Total Bytes: 32 bytes

3D Array (Tensor):
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
Shape: (2, 2, 2)
Dimensions: 3
Data Type: int64
Item Size: 8 bytes
Total Bytes: 64 bytes

'''