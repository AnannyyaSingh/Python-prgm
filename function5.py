#Increment 
counter = 0  # Global variable

def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment_counter()
increment_counter()
increment_counter()
