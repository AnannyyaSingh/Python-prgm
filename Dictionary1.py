#Grouping employes by depertments
employees = {
    "Alice": "HR",
    "Bob": "Engineering",
    "Charlie": "HR",
    "David": "Engineering",
    "Eve": "Marketing"
}
department_dict = {}
for employee, department in employees.items():
    if department not in department_dict:
        department_dict[department] = []
    department_dict[department].append(employee)
print(department_dict)