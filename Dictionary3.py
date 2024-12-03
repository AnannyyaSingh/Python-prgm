#categorised student as pass or fail
students = {
    "John": 45,
    "Alice": 75,
    "Bob": 50,
    "Charlie": 30,
    "David": 55
}

result = {}
for student, score in students.items():
    if score >= 50:
        result[student] = "Passed"
    else:
        result[student] = "Failed"

print(result)
