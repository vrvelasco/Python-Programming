# Victor Velasco (BookStore) 9/16/19

# Variables
TAX_RATE = 0.0975 # Constant
choice = 1
quantity = 0
price = 0.0
subtotal = 0.0
tax = 0.0
total = 0.0

while choice != 5:
    choice = int(input('Enter 1 for a Bbook\n' \
                       'Enter 2 for a DVD\n' \
                       'Enter 3 for a Blu-ray\n' \
                       'Enter 4 for a Graphic Novel\n' \
                       'Enter 5 to Exit'))

    if choice == 1:
        price = 7.99
        quantity = int(input('Enter the quantity of books purchased: '))
        subtotal += price * quantity
    elif choice == 2:
        price = 19.99
        quantity = int(input('Enter the quantity of DVDs purchased: '))
        subtotal += price * quantity
    elif choice == 3:
        price = 23.99
        quantity = int(input('Enter the quantity of Blu-rays purchased: '))
        subtotal += price * quantity
    elif choice == 4:
        price = 9.99
        quantity = int(input('Enter the quantity of Graphic Novels purchased: '))
        subtotal += price * quantity
    elif choice == 5:
        print('Good bye!')
    else:
            print('Incorrect entry, please try again.')

# Math
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display
print('Subtotal:  $', format(subtotal, ',.2f'))
print('Sales Tax: $', format(tax, ',.2f'))
print('Total:     $', format(total, ',.2f'))
