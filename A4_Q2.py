nested_tuple = []
n = int(input("Enter the number of inner tuples: "))

for i in range(n):
    inner_tuple = tuple(map(int, input(f"Enter elements of tuple {i + 1} separated by spaces: ").split()))
    nested_tuple.append(inner_tuple)

nested_tuple = tuple(nested_tuple)

# Flatten the nested tuple
flattened_tuple = tuple(item for sub_tuple in nested_tuple for item in sub_tuple)

print(f"Flattened Tuple: {flattened_tuple}")