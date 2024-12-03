#merging of two dict by using keys
dict1 = {'a': 5, 'b': 10, 'c': 15}
dict2 = {'b': 5, 'c': 10, 'd': 20}

merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print(merged_dict)
