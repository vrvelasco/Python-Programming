# Victor Velasco (IceCreamTruck) 9/9/19

TAX_RATE = 0.0975

print('Enter 1 for Eskimo Pie')
print('Enter 2 for Drumstick')
print('Enter 3 for Dreamsicle')
print('Enter 4 for Fudgesicle')
print('Enter 5 for Rainbow Bomb Pop')

choice = int(input('\nEnter your choice: '))

if choice == 1:
    price = 4.00
    qnty = int(input('\nEnter the quantity: '))
    subtotal = price * qnty
elif choice == 2:
    price = 5.50
    qnty = int(input('\nEnter the quantity: '))
    subtotal = price * qnty
elif choice == 3:
    price = 3.50
    qnty = int(input('\nEnter the quantity: '))
    subtotal = price * qnty
elif choice == 4:
    price = 3.50
    qnty = int(input('\nEnter the quantity: '))
    subtotal = price * qnty
elif choice == 5:
    price = 4.00
    qnty = int(input('\nEnter the quantity: '))
    subtotal = price * qnty
else:
    print('\nIncorrect entry')

sales_tax = TAX_RATE * subtotal
total = sales_tax + subtotal

print('\nSubtotal:  $' + format(subtotal, ',.2f'))
print('Sales Tax: $' + format(sales_tax, ',.2f'))
print('Total:     $' + format(total, ',.2f'))
