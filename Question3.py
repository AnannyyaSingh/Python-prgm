#Non-Local Variables
def outer():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    print(inner())
    print(inner())

outer()
