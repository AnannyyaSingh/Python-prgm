n = int(input("Enter the number of students: "))
students = []

for _ in range(n):
    name = input("Enter student's name: ")
    marks = int(input(f"Enter marks for {name}: "))
    students.append((name, marks))

students = tuple(students)

# Sort by marks in descending order
sorted_students = tuple(sorted(students, key=lambda student: student[1], reverse=True))

print(f"Sorted Tuple: {sorted_students}")
