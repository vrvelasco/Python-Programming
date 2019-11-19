# Victor Velasco (Cash Register Main) 11/18/19

import Retail
import CashRegister

PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

def main():
    pants = Retail.RetailItem('Pants', 10, 19.99)
    shirt = Retail.RetailItem('Shirt', 15, 12.50)
    dress = Retail.RetailItem('Dress', 3, 79.00)
    socks = Retail.RetailItem('Socks', 50, 1.00)
    sweater = Retail.RetailItem('Sweater', 5, 49.99)

    sale_items = { PANTS : pants, SHIRT : shirt, DRESS : dress, SOCKS : socks, SWEATER : sweater }

    register = CashRegister.CashRegister()

    checkout = 'n'

    while checkout.upper() == 'N':
        user_choice = get_user_choice()
        item = sale_items[user_choice]

        if item.get_inventory() == 0:
            print('The item is out of stock.')
        else:
            register.purchase_item(item)
            new_item = Retail.RetailItem(item.get_description(),\
                       item.get_inventory() - 1,\
                       item.get_price())

            sale_items[user_choice] = new_item
            
            checkout = input('Are you ready to checkout (Y/N)?')
    print()

    print('Your purchase total is: $',\
          format(register.get_total(), ',.2f'))

    print()

    register.show_items()
    register.clear()

def get_user_choice():
    print('Menu')
    print('------------')
    print('Enter 1 for Pants')
    print('Enter 2 for Shirt')
    print('Enter 3 for Dress')
    print('Enter 4 for Socks')
    print('Enter 5 for Sweater')

    choice = int(input('Enter the number of the item you wish to purchase.'))
    print()

    while choice > SWEATER or choice < PANTS:
        choice = int(input('Please enter a valid item number.'))
        
    return choice

# Call main
main()
