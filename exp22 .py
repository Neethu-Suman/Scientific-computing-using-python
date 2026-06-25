2. Basic arithmetic functions such as abs, sine, real, imag, complex, sinc etc. using bulit in modules.
# Importing the math and cmath modules
import math
import cmath
import numpy as np

# Absolute Value
a = abs(-5)  # 5
print(f"Absolute Value (abs(-5)): {a}")

# Sine (math module)
b = math.sin(math.pi / 2)  # 1.0
print(f"Sine (math.sin(math.pi / 2)): {b}")

# Real and Imaginary Parts of a Complex Number
c = complex(3, 4)  # 3 + 4j
real_part = c.real  # 3.0
imag_part = c.imag  # 4.0
print(f"Complex Number: {c}")
print(f"Real Part (c.real): {real_part}")
print(f"Imaginary Part (c.imag): {imag_part}")

# Creating Complex Numbers
d = complex(5, -7)  # 5 - 7j
print(f"Complex (complex(5, -7)): {d}")

# Sinc Function (Normalized Sinc using the math module)
def sinc(x):
    return math.sin(math.pi * x) / (math.pi * x) if x != 0 else 1

e = sinc(1)  # 0.6366197723675814
f = sinc(0)  # 1
print(f"Sinc (sinc(1)): {e}")
print(f"Sinc (sinc(0)): {f}")

# cmath functions for complex numbers
g = cmath.sin(c)  # Sine of a complex number
h = cmath.cos(c)  # Cosine of a complex number
i = cmath.exp(c)  # Exponential of a complex number
print(f"Sine of Complex (cmath.sin(complex(3, 4))): {g}")
print(f"Cosine of Complex (cmath.cos(complex(3, 4))): {h}")
print(f"Exponential of Complex (cmath.exp(complex(3, 4))): {i}")
