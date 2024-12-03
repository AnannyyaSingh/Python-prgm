#Complex Number Arithmetic
import cmath  # Importing the cmath module for polar coordinate conversions

# Input two complex numbers from the user
complex1 = complex(input("Enter the first complex number (e.g., 1+2j): "))
complex2 = complex(input("Enter the second complex number (e.g., 3+4j): "))

# 1. Addition
add_result = complex1 + complex2
print(f"Addition (Rectangular): {add_result}")
print(f"Addition (Polar): {cmath.polar(add_result)}")

# 2. Subtraction
sub_result = complex1 - complex2
print(f"Subtraction (Rectangular): {sub_result}")
print(f"Subtraction (Polar): {cmath.polar(sub_result)}")

# 3. Multiplication
mul_result = complex1 * complex2
print(f"Multiplication (Rectangular): {mul_result}")
print(f"Multiplication (Polar): {cmath.polar(mul_result)}")

# 4. Division
div_result = complex1 / complex2
print(f"Division (Rectangular): {div_result}")
print(f"Division (Polar): {cmath.polar(div_result)}")