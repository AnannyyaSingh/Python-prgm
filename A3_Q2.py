#program to count the frequency of each character in a string

s = "hello"
frequency = {}

for char in s:
     if char in frequency:
          frequency[char] += 1
     else:
          frequency[char] = 1

          print(frequency)