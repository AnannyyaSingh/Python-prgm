#accumulator
from functools import reduce

def accumulate(func, iterable):
    result = []
    def reducer(acc, x):
        res = func(acc, x)
        result.append(res)
        return res
    reduce(reducer, iterable)
    return result

print(accumulate(lambda acc, x: acc + x, [1, 2, 3, 4]))  # Output: [3, 6, 10]
