# Victor Velasco (Merlin Main) 12/1/19

import Owner

def main():
    # Variables
    name = ''
    address = ''
    phone_number = ''
    email = ''
    pet_name = ''
    pet_type = ''
    pet_age = 0
    charges = 0.0
    TAX = 0.0975

    # Get Customer Information
    print('CUSTOMER INFORMATION')
    name = input("Enter the Customer's name: ")
    address = input("Enter the Customer's address: ")
    phone_number = input("Enter the Customer's phone number: ")
    email = input("Enter the Customer's email address: ")

    customer = Owner.Customer(name, address, phone_number, email)

    # Get Pet Information
    print('\nPET INFORMATION')
    pet_name = input("Enter the Pet's name: ")
    pet_type = input('Enter the type of pet: ')
    pet_age = int(input("Enter the Pet's age: "))

    # Make sure the age is greater than or equal to 0
    while pet_age < 0:
        pet_age = int(input("Invalid age. Please enter the age again: "))
        
    pet = Owner.Pet(pet_name, pet_type, pet_age)

    # Get Service Details
    print('\nSERVICE DETAILS')
    charges = float(input('Enter the total cost of service(s): $'))
    while charges < 0:
        charges = float(input("Invalid charge amount. Please enter the amount again: $"))
        
    service = Owner.Invoice(charges, TAX)
    
    # Start Invoice
    print('\n' + ''.rjust(50,'═')) # Formatting
    print(" Merlin's Pet Grooming".ljust(33) + 'Customer Invoice')
    print(''.rjust(50,'═')) # Formatting
    
    # Display Customer Information
    print('\nCUSTOMER')
    print(''.rjust(50, '─')) # Formatting
    print(' Name:' + customer.get_name().rjust(43, '.'))
    print(' Address:' + customer.get_address().rjust(40, '.'))
    print(' Phone Number:' + customer.get_phone_number().rjust(35, '.'))
    print(' Email:' + customer.get_email().rjust(42, '.'))

    # Display Pet Information
    print('\nPET' )
    print(''.rjust(50, '─')) # Formatting
    print(' Name:' + pet.get_pet_name().rjust(43, '.'))
    print(' Type:' + pet.get_pet_type().rjust(43, '.'))
    print(' Age:' + str(pet.get_pet_age()).rjust(44, '.'))

    # Total
    print('\nCOST OF SERVICE(S)')
    print(''.rjust(50, '─')) # Formatting
    print(' Charges:' + ('$' + format(service.get_charges(), ',.2f')).rjust(40, '.'))
    print(' Tax:' + ('$' + format(service.get_tax(), ',.2f')).rjust(44, '.'))
    print(' Total:' + ('$' + format(service.get_total(), ',.2f')).rjust(42, '.'))

    # End Invoice
    print('\n' + ''.rjust(50,'═')) # Formatting
    print("Thank you for visiting Merlin's Pet Grooming!".rjust(48))
    print(''.rjust(50,'═')) # Formatting
    
# Call main
main()
