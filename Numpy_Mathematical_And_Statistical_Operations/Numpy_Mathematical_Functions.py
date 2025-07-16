import numpy as np

# Sample array
x = np.array([0, 1, 2, 3, 4, 5])
print("Original array:", x)

#  Exponential & Power Functions
print("np.exp(x):", np.exp(x))           # e^x
print("np.expm1(x):", np.expm1(x))       # e^x - 1 (better for small x)
print("np.power(x, 3):", np.power(x, 3)) # x^3
print("np.square(x):", np.square(x))     # x^2
print()

#  Logarithmic Functions
print("np.log(x+1):", np.log(x+1))       # natural log (log base e)
print("np.log10(x+1):", np.log10(x+1))   # log base 10
print("np.log2(x+1):", np.log2(x+1))     # log base 2
print()

#  Square Root / Cube Root
print("np.sqrt(x):", np.sqrt(x))         
print("np.cbrt(x):", np.cbrt(x))         
print()

#  Trigonometric Functions
angles = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(angles)  # Convert to radians
print("Angles in degrees:", angles)
print("In radians:", radians)
print("np.sin():", np.sin(radians))
print("np.cos():", np.cos(radians))
print("np.tan():", np.tan(radians))
print()

#  Absolute Value
neg = np.array([-1, -2, 0, 3])
print("Original:", neg)
print("np.abs():", np.abs(neg))
print("np.fabs():", np.fabs(neg))  # faster, always returns float
print()

#  Angle Conversions
deg = np.array([0, 90, 180])
rad = np.deg2rad(deg)
print("Degrees:", deg)
print("To Radians:", rad)
print("Back to Degrees:", np.rad2deg(rad))

# ================= NumPy Mathematical Functions Summary =================
# ✅ Exponential:   np.exp(), np.expm1()
# ✅ Logarithmic:   np.log(), np.log10(), np.log2()
# ✅ Roots:         np.sqrt(), np.cbrt()
# ✅ Power:         np.power(), np.square()
# ✅ Trigonometric: np.sin(), np.cos(), np.tan()
# ✅ Absolute:      np.abs(), np.fabs()
# ✅ Angle Conv:    np.deg2rad(), np.rad2deg()
# =========================================================================
'''
Mathematical Functions
Function	Description
np.exp(x)	Exponential of x (e^x)
np.log(x)	Natural log
np.log10(x)	Base-10 log
np.sqrt(x)	Square root
np.abs(x)	Absolute value
np.sin(x) / cos / tan	Trig functions
np.deg2rad(x)	Degrees to radians
np.rad2deg(x)	Radians to degrees

'''
