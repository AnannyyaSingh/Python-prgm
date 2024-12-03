#Find symmetric difference

set_A = set(map(int, input("Enter elements of set A separated by spaces: ").split()))
set_B = set(map(int, input("Enter elements of set B separated by spaces: ").split()))

# Calculate symmetric difference
symmetric_difference = set_A.symmetric_difference(set_B)
print(f"Symmetric difference of A and B: {symmetric_difference}")

# Update set A with the symmetric difference
set_A.symmetric_difference_update(set_B)
print(f"Set A after symmetric difference update: {set_A}")
