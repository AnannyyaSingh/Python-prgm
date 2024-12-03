# Python-prgm
This will contain python programs of different topics.
Basic Programs
Topic-1: Integer: basic operations
# integer and float 
int_value = 5      # Integer
float_value = 3.2  # Float
result = int_value + float_value  # Implicit conversion of int to float
print(result)  # Output: 8.2 (a float)


#Integer, float and complex
int_value1 = 5                # Integer
float_value1 = 3.2            # Float
complex_value = 2 + 3j       # Complex number

result_1 = int_value1 + complex_value  # Implicit conversion of int to complex
print(result_1)  # Output: (7+3j)

result2 = float_value1 + complex_value  # Implicit conversion of float to complex
print(result2)  # Output: (5.2+3j)

#Convert Boolean to string
#This will return True
# Example of converting boolean to string
bool_value1 = True
str_value1 = str(bool_value1)
print(str_value1)  # Output: "True"
print(type(str_value1))  # Output: <class 'str'>


#this will return false
bool_value2 = False
str_value2 = str(bool_value2)
print(str_value2)  # Output: "False"

#Convert String and the String "false" to Boolean
# Example of converting string to boolean
str_value3 = "true"
bool_value3 = bool(str_value3)
print(bool_value3)  # Output: True

str_value4 = "false"
bool_value4 = bool(str_value4)
print(bool_value4)  # Output: True, because it's a non-empty string

#Given a string "abc123" attempt to convert it to an integer. handle the exception if conversion fails. Why conversion fail and how it can be handled.

string_value = "abc123"

try:
    int_value = int(string_value)  # Attempt to convert the string to an integer
    print(int_value)
except ValueError as e:
    print(f"Conversion failed: {e}")  # Handle the exception if conversion fails

#Why the conversion fails?: 
#The string "abc123" contains both alphabetic characters (abc) and numeric characters (123).
#The int() function only works on strings that represent valid integers (e.g., "123", "-456"), 
#and it cannot handle mixed content like "abc123". Therefore, Python raises a ValueError.

#How it can be handled?: You can catch the ValueError using a try-except block, as shown in the code. 
#This allows you to gracefully handle the error instead of having the program crash. 
#You can also log or display an error message to indicate why the conversion failed.


# Accept the user's full name as input
full_name = input("Enter your full name: ")

# 1. Print the initials


# 2. Print the name in reverse order

# 3. Capitalize the first letter of each word

#Logical Operation
# Input two boolean values from the user (as 0 or 1)
bool1 = int(input("Enter first boolean (0 or 1): "))
bool2 = int(input("Enter second boolean (0 or 1): "))

# Convert 0/1 to boolean True/False
bool1 = bool(bool1)
bool2 = bool(bool2)

# Logical AND
and_result = bool1 and bool2
print(f"{bool1} AND {bool2} = {and_result}")

# Logical OR
or_result = bool1 or bool2
print(f"{bool1} OR {bool2} = {or_result}")

# Logical NOT for both values
not_bool1 = not bool1
not_bool2 = not bool2
print(f"NOT {bool1} = {not_bool1}")
print(f"NOT {bool2} = {not_bool2}")

# Logical XOR (exclusive OR)
xor_result = (bool1 and not bool2) or (not bool1 and bool2)  # Basic XOR logic
print(f"{bool1} XOR {bool2} = {xor_result}")

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

