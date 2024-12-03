#Counting frequency in string
string = "Hello, World!"
char_count = {}

for char in string:
        char = char.lower()  # Make case insensitive
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print(char_count)
