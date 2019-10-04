# Victor Velasco (AreaCalculator) 9/30/19
from AreaFunctions import *

def main():
    choice = 0
    displayMenu()
    choice = int(input('Enter your choice: '))

    while choice != 5:
        if choice == 1:
            square()
        elif choice == 2:
            rectangle()
        elif choice == 3:
            circle()
        elif choice == 4:
            triangle()
        else:
            print('Incorrect entry. \nTry again.')

            # Display menu
        displayMenu()
        choice = int(input('Enter your choice: '))
            
main() # Call main
