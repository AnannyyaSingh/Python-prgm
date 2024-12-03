# Furniture items and their costs
furniture_prices = {
    "Sofa set": 20000,
    "Dining table": 8500,
    "T.V. Stand": 4599,
    "Cupboard": 13920
}

# Initialize required furniture and quantity
required_furniture = "Sofa set"  # Example
required_quantity = 2  # Example

# Calculate the bill amount
if required_furniture in furniture_prices and required_quantity > 0:
    bill_amount = furniture_prices[required_furniture] * required_quantity
    print(f"Bill amount for {required_quantity} {required_furniture}(s): Rs. {bill_amount}")
else:
    print("Invalid furniture or quantity. Bill amount: Rs. 0")
