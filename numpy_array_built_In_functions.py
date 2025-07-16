import numpy as np

# Zeros - Array Filled with 0's
arr_zeros=np.zeros((2,3))
print("Zeros Array: \n ",arr_zeros,"\n")

# Ones - Array filled with 1's
arr_ones=np.ones((3,2))
print("Ones Array:\n",arr_ones,"\n")

#Empty - Array With Uninitialised values (may contain garbage values)
arr_empty= np.empty((2,2))
print("Empty Array (random initial values):\n",arr_empty,"\n")

#Full-array Filled With A Specific Value
arr_full = np.full((2,3),7)
print("Full Array (with 7s):\n",arr_full,"\n")

#Arange - array with a range of numbers 
arr_arrange = np.arange(0,10,2)  #start = 0 , stop = 10 , step = 2 
print("Arrange Array:\n",arr_arrange,"\n")

# Linspace - Evenly spaced values over a range
arr_linspace = np.linspace(0,1,5) # 5 values from 0 to 1
print("Linspace Array:\n",arr_linspace,"\n")

# Eye - Identity Matrix
arr_eye = np.eye(3)
print("Identity Matrix (eye):\n",arr_eye,"\n")

# Random - Array with random values between 0 and 1
arr_random = np.random.rand(2,2)
print("Random Array: \n",arr_random,"\n")

#Random-Integers from 1 to 9
arr_random_int = np.random.randint(1,10,(2,2))
print("Random Intgers:\n",arr_random_int,"\n")

'''
Summary of Functions
Function	Purpose
np.zeros(shape)	Array of all 0s
np.ones(shape)	Array of all 1s
np.empty(shape)	Array with uninitialized values
np.full(shape, value)	Array with a specific constant
np.arange(start, stop, step)	Array with range of values
np.linspace(start, stop, num)	Evenly spaced values
np.eye(N)	Identity matrix (NxN)
np.random.rand(shape)	Random float values in [0.0, 1.0)

'''