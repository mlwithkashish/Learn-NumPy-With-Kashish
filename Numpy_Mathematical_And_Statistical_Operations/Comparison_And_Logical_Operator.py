
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

#  Comparison
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a <= b:", a <= b)

#  Logical Operations
print("(a > 2) & (a < 5):", (a > 2) & (a < 5))
print("(a < 2) | (b > 4):", (a < 2) | (b > 4))
print("~(a == 3):", ~(a == 3))

#  Logical Functions
print("np.all(a > 0):", np.all(a > 0))           # True
print("np.any(b == 3):", np.any(b == 3))         # True
print("np.where(a % 2 == 0):", np.where(a % 2 == 0))  # even positions

# ============== NumPy Comparison & Logical Ops ==================
#  Comparison: ==, !=, >, <, >=, <= → returns Boolean arrays
#  Logical Ops: & (and), | (or), ~ (not), np.logical_xor()
#  Functions:
#     np.all(condition) → True if all match
#     np.any(condition) → True if any match
#     np.where(condition) → positions where condition is True
# ================================================================


