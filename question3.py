#chain Operations

def chain_operations(functions, iterable):
    for func in functions:
        if func.__name__ == "filter":
            iterable = filter(func, iterable)
        else:
            iterable = map(func, iterable)
    return list(iterable)


chain_funcs = [lambda x: x > 2, lambda x: x * 2]
print(chain_operations(chain_funcs, [1, 2, 3, 4]))  # Output: [6, 8]
