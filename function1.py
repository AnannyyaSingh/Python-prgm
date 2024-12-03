#print info function
def print_info(*args, **kwargs):
    # Part a: new line
    for arg in args:
        print(arg)
    # Part b: Print each keyword argument in the format key: value
    for key, value in kwargs.items():
        print("{key}: {value}")

print_info("Alice", "Bob", age=25, location="New York")
