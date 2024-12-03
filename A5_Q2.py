#remove non-integer elements
data_set = input("Enter elements of the set (use spaces to separate, include different types like strings, floats): ").split()

# Initialize an empty set to store mixed data
mixed_data_set = set()

# Convert each element to an integer if possible, otherwise keep it as it is
for item in data_set:
    if item.isdigit():  # Check if the item is a digit
        mixed_data_set.add(int(item))  # Convert to integer and add to the set
    else:
        mixed_data_set.add(item)  # Add the item as-is (it remains a string)

# Initialize an empty set for filtered results
filtered_set = set()

# Filter out non-integer elements
for item in mixed_data_set:
    if type(item) == int:  # Check if the item is an integer
        filtered_set.add(item)  # Add integer item to filtered_set

# Print the filtered set with only integer elements
print(f"Set after removing non-integer elements: {filtered_set}")
