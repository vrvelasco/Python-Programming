# Victor Velasco 8/26/19

# Variables
tomatoes = 1.99
zuchinni = 2.99
peppers = 1.49
carrots = 0.89
potatoes = 1.39
onions = 2.99
subtotal = 0.0
tax = 0.0
total = 0.0
TAX_RATE = 0.0925
qnty = 0.0
choice = 0

# Menu
print('Enter 1 for tomatoes\nEnter 2 for zuchinni\nEnter 3 for peppers\n' +
         'Enter 4 for carrots\nEnter 5 for potatoes\nEnter 6 for onions\n')
choice = int(input('Enter your choice: '))

# IF Statement
if choice == 1:
    qnty = float(input('Enter pounds purchased: '))
    subtotal = tomatoes * qnty
elif choice == 2:
    qnty = float(input('Enter pounds purchased: '))
    subtotal = zuchinni * qnty
elif choice == 3:
    qnty = float(input('Enter pounds purchased: '))
    subtotal = peppers * qnty
elif choice == 4:
    qnty = float(input('Enter pounds purchased: '))
    subtotal = carrots * qnty
elif choice == 5:
    qnty = float(input('Enter pounds purchased: '))
    subtotal = potatoes * qnty
elif choice == 6:
    qnty = float(input('Enter pounds purchased: '))
    subtotal = onions * qnty
else:
    print('Incorrect entry')

# Math
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display results
if subtotal > 0.0:
    print('Subtotal:  $' + format(subtotal, ',.2f'))
    print('Sales tax: $' + format(tax, ',.2f'))
    print('Total:       $' + format(total, ',.2f'))
    
