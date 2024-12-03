# Input a number from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 3 or 7
if number % 3 == 0 and number % 7 == 0:
    print(f"{number} is divisible by both 3 and 7.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3.")
elif number % 7 == 0:
    print(f"{number} is divisible by 7.")
else:
    print(f"{number} is not divisible by 3 or 7.")
