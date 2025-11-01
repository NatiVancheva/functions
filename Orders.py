coffee_price = 1.50
coke_price = 1.40
water_price = 1.00
snacks_price = 2.00
def calculate_price(product, quantity):
    return {
        "coffee": coffee_price * quantity,
        "coke": coke_price * quantity,
        "water": water_price * quantity,
        "snacks": snacks_price * quantity
    }.get(product, "Invalid product!")

product = input("Enter a product: ")
quantity = int(input("Enter quantity: "))
result = calculate_price(product, quantity)
print(f"Result: {result :.2f}")
