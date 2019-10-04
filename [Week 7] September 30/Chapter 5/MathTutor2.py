# Victor Velasco (MathTutor2) 9/30/2019

import random

num1 = 0
num2 = 0
userNum = 0
answer = 0
choice = 0

def main():
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

# Methods
def displayMenu():
    print('Enter 1 for addition')
    print('Enter 2 for subtraction')
    print('Enter 3 for multiplication')
    print('Enter 4 to exit')

def addition(num1, num2):
    print(num1, '+', num2, '=')
    userNum = int(input('Enter your answer: '))
    answer = num1 + num2
    if(answer == userNum):
        print('Correct answer, good job!')
    else:
        print('Incorrect answer.')

def subtraction(num1, num2):
    print(num1, '-', num2, '=')
    userNum = int(input('Enter your answer: '))
    answer = num1 - num2
    if(answer == userNum):
        print('Correct answer, good job!')
    else:
        print('Incorrect answer.')

def multiplication(num1, num2):
    print(num1, '*', num2, '=')
    userNum = int(input('Enter your answer: '))
    answer = num1 * num2
    if(answer == userNum):
        print('Correct answer, good job!')
    else:
        print('Incorrect answer.')

# Call main
main()
