import numpy as np

# Original Float array
arr_float = np.array([1.7,2.3,3.9])
arr_int = arr_float.astype(np.int32) # Float to integer
print("Float to Integer: ",arr_int)

# Integer to Float
arr_int2=np.array([1,2,3])
arr_float2 = arr_int2.astype(np.float64)
print("Integer To Float: ",arr_float2)

# Integer To Boolean
arr_bool = arr_int2.astype(bool)
print("Integer to Boolean: ",arr_bool)

# Integer To String
arr_str = arr_int2.astype(str)
print("Integer to String:",arr_str)

# String to Float (if numeric)
arr_numeric_str = np.array(['1.5','2.5','3.0'])
arr_str_to_float = arr_numeric_str.astype(float)
print("String To Float:",arr_str_to_float)

# Boolean To Integer
arr_bool2 = np.array([True,False,True])
arrr_bool_to_int = arr_bool2.astype(int)
print("Boolean to Integer: " , arrr_bool_to_int)

'''
What is Type Casting in NumPy?
Type Casting is the process of converting the data type of the elements in a NumPy array.

Use .astype() method to do this.

It does not change the original array — it returns a new array.

Common Use Cases
Convert float to int

Convert int to float

Convert number to string

Convert string to float (if possible)

Convert to bool (non-zero = True)


'''