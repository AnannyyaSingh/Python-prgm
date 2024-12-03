fruits = tuple(input("Enter elements of tuple separated by spaces: ").split())
print(type(fruits))
# Converting tuple to list, add element from user, and convert back to tuple
fruits_list = list(fruits)
new_fruit = input("Enter the fruit to add: ")
fruits_list.append(new_fruit)
updated_fruits = tuple(fruits_list)

print(f"Updated Tuple: {updated_fruits}")