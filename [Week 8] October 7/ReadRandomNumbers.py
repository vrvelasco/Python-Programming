# Victor Velasco (Read Random Numbers) 10/7/19

def main():
    counter = 0
    total = 0
    number = 0

    inputFile = open('random_numbers.txt', 'r')

    for line in inputFile:
        number = int(line)
        total += number
        counter +=1

    inputFile.close()

    print('Total:', format(total, ','))
    print(counter, 'numbers were read from the file.')

main()
