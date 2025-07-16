import numpy as np
 
 # 1 Auto Detected Integer array ( default : int 3 or int 64 depending on system)
arr_int = np.array([1,2,3])
print("Default Integer Array: ", arr_int)
print("Data Type : ",arr_int.dtype)
print("Item Size: ",arr_int.itemsize,"bytes\n")

 # 2 Specify float32
arr_float = np.array([1,2,3], dtype=np.float32)
print("Float32 Array:",arr_float)
print("Data Type: ",arr_float.dtype)
print("Item Size: ",arr_float.itemsize,"bytes\n")

 # 3 Boolean Type
arr_bool = np.array([True, False, True])
print("Boolean Array:", arr_bool)
print("Data Type:", arr_bool.dtype)
print("Item Size:", arr_bool.itemsize, "bytes\n")

# 4️ String array
arr_str = np.array(["apple", "banana", "cherry"])
print("String Array:", arr_str)
print("Data Type:", arr_str.dtype)
print("Item Size (bytes per char * max string length):", arr_str.itemsize, "\n")

# 5 Complex number array
arr_complex = np.array([1 + 2j, 3 + 4j])
print("Complex Array:", arr_complex)
print("Data Type:", arr_complex.dtype)
print("Item Size:", arr_complex.itemsize, "bytes\n")

# 6 Convert float to int using astype
arr_original = np.array([1.9, 2.5, 3.1])
arr_converted = arr_original.astype(np.int32)
print("Original Float Array:", arr_original)
print("Converted to Integer:", arr_converted)
print("New Data Type:", arr_converted.dtype, "\n")

# 7 Compare memory usage
print("Memory Usage Comparison:")
print("int32 Array:   ", np.array([1, 2, 3], dtype=np.int32).nbytes, "bytes")
print("float64 Array: ", np.array([1, 2, 3], dtype=np.float64).nbytes, "bytes")
print("bool Array:    ", np.array([True, False, True], dtype=np.bool_).nbytes, "bytes")

'''
.dtype → Data type of the array

.itemsize → Memory per element (in bytes)

.astype() → Convert from one type to another

.nbytes → Total memory used by the array


'''
