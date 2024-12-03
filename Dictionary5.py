#Employes with highest salary in each dePARTMENT.
employees = {
    "HR": {
        "Alice": {"age": 30, "position": "Manager", "salary": 50000},
        "Bob": {"age": 25, "position": "Executive", "salary": 40000}
    },
    "Engineering": {
        "Charlie": {"age": 35, "position": "Lead", "salary": 70000},
        "David": {"age": 28, "position": "Engineer", "salary": 60000}
    },
    "Marketing": {
        "Eve": {"age": 29, "position": "Coordinator", "salary": 45000}
    }
}

highest_salary = {}
for department, employees_info in employees.items():
    max_salary = 0
    top_employee = None
    for employee, details in employees_info.items():
        if details["salary"] > max_salary:
            max_salary = details["salary"]
            top_employee = employee
    highest_salary[department] = top_employee

print(highest_salary)
