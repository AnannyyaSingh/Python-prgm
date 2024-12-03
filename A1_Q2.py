#Convert Boolean to string
#This will return True
# Example of converting boolean to string
bool_value1 = True
str_value1 = str(bool_value1)
print(str_value1)  # Output: "True"
print(type(str_value1))  # Output: <class 'str'>


#this will return false
bool_value2 = False
str_value2 = str(bool_value2)
print(str_value2)  # Output: "False"

#Convert String and the String "false" to Boolean
# Example of converting string to boolean
str_value3 = "true"
bool_value3 = bool(str_value3)
print(bool_value3)  # Output: True

str_value4 = "false"
bool_value4 = bool(str_value4)
print(bool_value4)  # Output: True, because it's a non-empty string
