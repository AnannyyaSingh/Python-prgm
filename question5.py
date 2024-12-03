#compose

def compose(f, g):
    return lambda x: f(g(x))


f = lambda x: x + 2
g = lambda x: x * 3
composed_func = compose(f, g)
print(composed_func(4))  # Output: 14
