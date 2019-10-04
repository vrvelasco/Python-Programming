# Victor Velasco (Func) 9/30/19

# Functions (Methods)
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
