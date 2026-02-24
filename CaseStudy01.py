# Grocery Billing System

# Item 1
price1 = float(input("Enter price of item 1: "))
qty1 = int(input("Enter quantity of item 1: "))

# Item 2
price2 = float(input("Enter price of item 2: "))
qty2 = int(input("Enter quantity of item 2: "))

# Item 3
price3 = float(input("Enter price of item 3: "))
qty3 = int(input("Enter quantity of item 3: "))

# Item 4
price4 = float(input("Enter price of item 4: "))
qty4 = int(input("Enter quantity of item 4: "))

# Item 5
price5 = float(input("Enter price of item 5: "))
qty5 = int(input("Enter quantity of item 5: "))

# Calculate total
total = (price1 * qty1) + (price2 * qty2) + (price3 * qty3) + (price4 * qty4) + (price5 * qty5)

# Apply discount
if total > 100:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

# Display results
print("\nOriginal Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)