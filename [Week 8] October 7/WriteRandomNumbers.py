# Victor Velasco (Write Random Numbers) 10/7/19

import random

def main():
    # Variables
    fileName = ''
    numberOfRandoms = 0
    randomNumber = 0

    fileName = input('Enter the name of the file to which results should be written: ')
    numberOfRandoms = int(input('Enter the number of random numbers to be written to the file: '))

    while numberOfRandoms < 1:
        print('Incorrect entry.\nTry again.')
        numberOfRandoms = int(input('Enter a number greater than zero: '))

    outputFile = open(fileName, 'w')

    for counter in range(numberOfRandoms):
        randomNumber = random.randint(1, 500)
        outputFile.write(str(randomNumber) + '\n')

    outputFile.close()

main()
