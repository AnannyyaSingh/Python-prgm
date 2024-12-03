#accept multiple set and return union of unique element set
# Input from user
num_of_sets = int(input("Enter number of sets: "))
sets = []

for i in range(num_of_sets):
    s = set(map(int, input(f"Enter elements of set {i+1} separated by spaces: ").split()))
    sets.append(s)

# Calculate union
union_result = set()
for s in sets:
    union_result = union_result.union(s)

print(f"Union of all sets: {union_result}")