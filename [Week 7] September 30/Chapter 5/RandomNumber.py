# Victor Velasco (RandomNumber) 9/13/19

import random

def main():
    number = 0
    play = 1

    while play > 0:
        number = random.randint(1, 100)
        play = playGuessingGame(number)
    print('Thanks for playing!')

def playGuessingGame(number):
    userGuess = int(input('Enter a number between 1 and 100. \nEnter zero to quit.'))

    while userGuess > 0:
        if userGuess > number:
            print('Too high, try again.')
            userGuess = int(input('Enter a number between 1 and 100. \nEnter zero to quit.'))
        elif userGuess < number:
             print('Too low, try again.')
             userGuess = int(input('Enter a number between 1 and 100. \nEnter zero to quit.'))
        else:
             print('Congratulations, you guess the number! =)')
             return userGuess
        return userGuess
main() # Call main
            
