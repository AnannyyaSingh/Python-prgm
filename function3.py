#apply operation
def apply_operation(func, numbers):
    return [func(num) for num in numbers]


result = apply_operation(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(result)