# Victor Velasco (MathTutor3) 9/30/2019

import random
from func import *

def main():
    # Variables
    num1 = 0
    num2 = 0
    choice = 0
    
    displayMenu()
    choice = int(input('Enter your choice: '))

    while(choice != 4):
        # Generate random numbers
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # Option chosen
        if(choice == 1):
            addition(num1, num2)
        elif(choice == 2):
            subtraction()
        elif(choice == 3):
            multiplication()
        else:
            print('Incorrect entry. \nPlease try again: ')

        # Display menu
        displayMenu()
        choice = int(input('Enter your choice: '))

# Call main
main()
