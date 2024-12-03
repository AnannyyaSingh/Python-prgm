tuple1 = tuple(map(int, input("Enter elements of first tuple separated by spaces: ").split()))
tuple2 = tuple(map(int, input("Enter elements of second tuple separated by spaces: ").split()))

print()
common_elements = tuple(set(tuple1).intersection(tuple2)) #common elements

print(f"Common elements: {common_elements}")
