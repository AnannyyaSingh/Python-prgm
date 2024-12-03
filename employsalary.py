# Input employee's salary and years of service
salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the employee's years of service: "))

# Calculate bonus based on salary and years of service
if salary > 50000:
    if years_of_service > 5:
        bonus = salary * 0.10  # 10% bonus
    else:
        bonus = 0  # No bonus if less than 5 years of service
else:
    bonus = salary * 0.15  # 15% bonus

# Display the bonus
print(f"The employee's bonus is: {bonus}")
