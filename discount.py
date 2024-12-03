# Input: Price of the product
price = float(input("Enter the price of the product: "))

# Input: Check if the customer is a premium member
is_premium_member = input("Is the customer a premium member? (yes/no): ").strip().lower()

# Initialize discount
discount = 0

# Calculate discount based on price
if price > 1000:
    discount = 0.20  # 20% discount
elif 500 <= price <= 1000:
    discount = 0.10  # 10% discount
else:
    discount = 0.05  # 5% discount

# Additional discount for premium members
if is_premium_member == 'yes':
    discount += 0.05  # Add 5% additional discount

# Calculate the total discount amount
discount_amount = price * discount

# Calculate the final price after discount
final_price = price - discount_amount

# Output the results
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price after Discount: ${final_price:.2f}")
