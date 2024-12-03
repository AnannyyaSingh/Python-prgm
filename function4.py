#lambda function

# Part 1: Using map to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squared_numbers)

# Part 2: Using filter to keep only even numbers in the list
even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
print(even_numbers)
