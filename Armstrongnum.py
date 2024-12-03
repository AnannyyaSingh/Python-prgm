start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    digits = len(str(num))
    sum_of_powers = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
    if num == sum_of_powers:
        print(num)


