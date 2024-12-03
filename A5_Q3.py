#accept two sets and return true if one set is proper subset of other

set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))

# Check if one is a proper subset of the other
result = set1 < set2 or set2 < set1
print(f"Is one set a proper subset of the other? {result}")
