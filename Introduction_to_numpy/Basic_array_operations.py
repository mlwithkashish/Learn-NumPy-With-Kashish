import numpy as np

# Create two arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

#  Element-wise Addition
print("Addition:       ", a + b) #[ 11 22 33 44]

#  Element-wise Subtraction
print("Subtraction:    ", a - b) #[ 9 18 27 36]

#  Element-wise Multiplication
print("Multiplication: ", a * b) #[10 40 90 160]

#  Element-wise Division
print("Division:       ", a / b) #[10. 10. 10. 10.]

# ️ Element-wise Floor Division
print("Floor Division: ", a // b) #[10 10 10 10]

#  Element-wise Power
print("Power:          ", a ** 2) #[100 400 900 1600]

#  Modulo Operation
print("Modulo:         ", a % b) #[ 0 0 0 0 ]

#  Comparison (Element-wise)
print("Greater than 20:", a > 20) #[False False True True]
print("Equal to 30:    ", a == 30) #[False False True False]

#  Dot Product (Matrix-style multiplication)
dot_product = np.dot(a, b)
print("Dot Product:    ", dot_product) #[300]

#  Aggregate Functions
print("Sum:            ", a.sum()) #100
print("Min:            ", a.min()) #10
print("Max:            ", a.max()) #40
print("Mean:           ", a.mean()) #25.0
print("Std Dev:        ", a.std()) #11.180......

#  Array-wise operations
print("a squared:      ", np.square(a)) #[ 100 400 900 1600]
print("Square root:    ", np.sqrt(a)) #[ 3.16....  4.42.....   5.47...   6.32....]

# ======================== NumPy Array Operations Summary ========================
#  Element-wise Operations: +, -, *, /, //, %, ** 
#  Comparison: >, <, ==, !=, >=, <= → returns boolean arrays
#  Mathematical Functions: np.sqrt(), np.square(), np.exp(), np.log()
#  Aggregates: sum(), min(), max(), mean(), std(), var()
#  Dot Product: np.dot(a, b)
#  Type Casting: a.astype(new_type)
#  Memory Info: a.dtype, a.itemsize, a.nbytes
#  Broadcasting: smaller arrays are "stretched" to match shapes in operations
# =================================================================================
