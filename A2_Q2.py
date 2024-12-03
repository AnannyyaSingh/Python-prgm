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
