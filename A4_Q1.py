import sys

elements = list(map(int, input("Enter list elements separated by spaces: ").split()))
tuple_elements = tuple(elements)

# Size of list and tuple
list_size = sys.getsizeof(elements)
tuple_size = sys.getsizeof(tuple_elements)

print(f"Size of List: {list_size} bytes")
print(f"Size of Tuple: {tuple_size} bytes")