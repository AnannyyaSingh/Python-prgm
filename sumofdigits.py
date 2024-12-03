# Input a number from the user
num = int(input("Enter a number: "))
sum_digits = 0

# Loop to calculate sum of digits
while num > 0:
    digit = num % 10  # Get the last digit
    sum_digits += digit  # Add the digit to sum
    num = num // 10  # Remove the last digit

# Output the result
print("The sum of the digits is:", sum_digits)
