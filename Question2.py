#Shadow Variable Usage
y = 50

def function_a():
    y = 30
    print(f"Function A y: {y}")

def function_b():
    global y
    y = 70
    print(f"Function B y: {y}")

function_a()
function_b()
print(f"Global y: {y}")
