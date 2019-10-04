# Victor Velasco (MathTutor) 9/30/2019

import random

num1 = 0
num2 = 0
userNum = 0
answer = 0
choice = 0

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print('Enter 1 for addition')
print('Enter 2 for subtraction')
print('Enter 3 for multiplication')
print('Enter 4 to exit')

choice = int(input('Enter your choice: '))

while(choice != 4):
    if(choice == 1):
        print(num1, '+', num2, '=')
        userNum = int(input('Enter your answer: '))
        answer = num1 + num2
        if(answer == userNum):
            print('Correct answer, good job!')
        else:
            print('Incorrect answer.')
    elif(choice == 2):
        print(num1, '-', num2, '=')
        userNum = int(input('Enter your answer: '))
        answer = num1 - num2
        if(answer == userNum):
            print('Correct answer, good job!')
        else:
            print('Incorrect answer.')
    elif(choice == 3):
        print(num1, '*', num2, '=')
        userNum = int(input('Enter your answer: '))
        answer = num1 * num2
        if(answer == userNum):
            print('Correct answer, good job!')
        else:
            print('Incorrect answer.')
    else:
        print('Incorrect entry. \nPlease try again: ')
    # Display menu
    print('Enter 1 for addition')
    print('Enter 2 for subtraction')
    print('Enter 3 for multiplication')
    print('Enter 4 to exit')

    choice = int(input('Enter your choice: '))
