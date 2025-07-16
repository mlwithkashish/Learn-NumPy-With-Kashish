import numpy as np

# Sample Data
data = np.array([10 , 15, 20 , 25 , 30 , 35 , 40])
print("Data:",data)

# 01 Basic Statistics
print("Mean:",np.mean(data)) #25.0
print("Median:", np.median(data))       # 25.0
print("Min:", np.min(data))             # 10
print("Max:", np.max(data))             # 40

#  Spread/Dispersion
print("Standard Deviation:", np.std(data))   # ~9.35
print("Variance:", np.var(data))             # ~87.76

#  Percentile / Quantile
print("25th Percentile:", np.percentile(data, 25))  # 17.5
print("75th Percentile:", np.percentile(data, 75))  # 32.5
print("Quantile 0.5:", np.quantile(data, 0.5))       # 25.0

#  Index of max/min
print("Index of Max:", np.argmax(data))       # 6
print("Index of Min:", np.argmin(data))       # 0

# ============== NumPy Statistical Summary ====================
#  np.mean(), np.median() → average & middle
#  np.std(), np.var()     → spread / dispersion
#  np.min(), np.max()     → extreme values
#  np.percentile(arr, p)  → value at p-th percentile
#  np.quantile(arr, q)    → same as percentile (q = p / 100)
#  np.argmax(), np.argmin() → position of max/min
# ==============================================================

'''
Key Statistical Functions
Function	Purpose
np.mean()	Average of elements
np.median()	Median (middle value)
np.std()	Standard deviation
np.var()	Variance
np.min() / np.max()	Minimum / Maximum
np.percentile()	Value at a given percentile (e.g. 25th)
np.quantile()	Value at a given quantile (e.g. 0.75)
np.argmax()	Index of max value
np.argmin()	Index of min value


'''