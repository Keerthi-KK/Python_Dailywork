# Program to calculate total cost and apply discount if applicable

quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))
total_cost = quantity * price_per_item

if total_cost > 1000:
    discount = total_cost * 0.10
    cost_price= total_cost - discount
    print(f"Discount applied: Rs. {discount}")
else:
    print("No discount applied.")
    cost_price = total_cost

print(f"Total cost to pay:Rs.{cost_price}")
