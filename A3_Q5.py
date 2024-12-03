#program to find the longest word in a string.
s = "The quick brown fox jumped over the lazy dog"
words = s.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)  # Output: jumped