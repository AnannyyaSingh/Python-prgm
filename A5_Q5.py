# intersection of all sets

num_of_sets = int(input("Enter number of sets: "))
sets = []

for i in range(num_of_sets):
    s = set(map(int, input(f"Enter elements of set {i+1} separated by spaces: ").split()))
    sets.append(s)

# Calculate intersection
if sets:
    intersection_result = sets[0] #so as to not take garbage value
    for s in sets[1:]: 
        intersection_result = intersection_result.intersection(s)
else:
    intersection_result = set()

print(f"Intersection of all sets: {intersection_result}")
