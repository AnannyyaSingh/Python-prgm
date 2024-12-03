#Function Return and Global Modification
result = 0

def calculate():
    global result
    for i in range(1, 5):
        result += i
    return result

print(calculate())
print(result)