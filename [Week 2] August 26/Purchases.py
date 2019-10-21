# Victor Velasco 8/26/19

# Variables
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0
subTotal = 0.0
tax = 0.0
total = 0.0
TAX_RATE = 0.0925 # Constant

# Get price
item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
item4 = float(input("Enter the price of item 4: "))
item5 = float(input("Enter the price of item 5: "))

# Math
subTotal = item1 + item2 + item3 + item4 + item5
tax = subTotal * TAX_RATE
total = subTotal + tax

print("Subtotal: $" + format(subTotal, ',.2f'))
print("Sales tax: $" + format(tax, ',.2f'))
print("Total: $" + format(total, ',.2f'))
