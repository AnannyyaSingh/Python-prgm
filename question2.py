#custome function

def custom_map(functions, iterable):
    result = []
    for item in iterable:
        for func in functions:
            item = func(item)
        result.append(item)
    return result

map_funcs = [lambda x: x + 1, lambda x: x * 2]
print(custom_map(map_funcs, [1, 2, 3]))  # Output: [4, 6, 8]
