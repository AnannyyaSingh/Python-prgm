#Program to swap the first and last character of a string

s = "python"

if len(s)>1:
    s = s[-1] + s[1:-1] + s[0]

    print (s)