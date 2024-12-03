#fibonacci series upto 50  

# Generate Fibonacci numbers up to 50
fibonacci_set = set()
a, b = 0, 1
while a <= 50:
    fibonacci_set.add(a)
    a, b = b, a + b

# Generate even numbers up to 50
even_set = {x for x in range(51) if x % 2 == 0}

# Find intersection
intersection = fibonacci_set.intersection(even_set)
print(f"Intersection of Fibonacci and even numbers up to 50: {intersection}")
