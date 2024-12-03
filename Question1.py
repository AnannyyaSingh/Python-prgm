#Global Variable
x = 10

def outer_function():
    x = 5

    def inner_function():
        global x
        x += 1
        print(f"Inner x: {x}")

    inner_function()
    print(f"Outer x: {x}")

outer_function()
print(f"Global x: {x}")
