# Victor Velasco (Customer Main) 11/25/19

import Person

def main():
    # Local variables
    name = ''
    address = ''
    phone_number = ''
    cust_number = 0
    on_list_flag = False

    # Get Customer Information
    name = input("Enter the Customer's name: ")
    address = input("Enter the Customer's address: ")
    phone_number = input("Enter the Customer's phone number: ")
    cust_number = input("Enter the Customer's ID number: ")
    on_list = input("Does the Customer wish to be on the mailing list?" +
                    "\nEnter Yes or No: ")

    if on_list == 'Yes':
        on_list_flag = True
    else:
        on_list_flag = False

    customer = Person.Customer(name, address, phone_number, cust_number, on_list_flag)

    # Display Customer Information
    print('\nCustomer Information: ')
    print('Name: ' + customer.get_name())
    print('Address: ' + customer.get_address())
    print('Customer Number: ' + customer.get_cust_number())
    print('On List: ' + str(customer.get_on_list()))

# Call main
main()
