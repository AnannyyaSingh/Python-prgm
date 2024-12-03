# Input a single character from the user
char = input("Enter an alphabet: ").lower()

# Check if the input is an alphabet
if char.isalpha() and len(char) == 1:
    # Check if the character is a vowel
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Please enter a valid alphabet.")
