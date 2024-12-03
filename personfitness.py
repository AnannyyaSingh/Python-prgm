# Input the person's age and weight
age = int(input("Enter the person's age: "))
weight = float(input("Enter the person's weight in kg: "))

# Check the person's fitness based on age and weight
if (18 <= age <= 40) and (50 <= weight <= 70):
    print("The person is fit.")
elif age < 18 or age > 40:
    if weight > 100:
        print("The person is overweight.")
    else:
        print("The person is unfit.")
else:
    print("The person is unfit.")
