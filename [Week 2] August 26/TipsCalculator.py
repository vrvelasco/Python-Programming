# Victor Velasco 8/26/19

# Variables
food = 0.0
tip = 0.0
tax = 0.0
total = 0.0

# Constants
TAX_RATE = 0.0925
TIP_RATE = 0.2

# Math
food = float(input('Enter the cost of the food: '))
tip = food * TIP_RATE
tax = food * TAX_RATE
total = food + tip + tax

# Display
print("Tip:      $" + format(tip, ',.2f'))
print("Tax:     $" + format(tax, ',.2f'))
print("Total:   $" + format(total, ',.2f'))
