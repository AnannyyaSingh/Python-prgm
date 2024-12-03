# Input the sides of the triangle
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Check if it's a valid triangle
if (a + b > c) and (b + c > a) and (c + a > b):
    # Classify the triangle
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or c == a:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")
