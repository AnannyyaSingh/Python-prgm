#Program to check if a given string is a palindrome(reads forward and backward)

s1 = "hello"
s2 = "madam"
s1 = s1.lower().replace(" ","")
s2 = s2.lower().replace(" ","")
is_palindrome1 = s1 ==s1[::-1]

print(is_palindrome1)