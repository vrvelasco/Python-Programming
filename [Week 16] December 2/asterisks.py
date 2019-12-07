# Victor Velasco (Asterisks) 12/2/2019

def main():
    number = 0

    number = int(input('How many lines to display?: '))

    print_lines(number)

def print_lines(n):
    if n > 1:
        print_lines(n - 1)


    for i in range(n):
        print('*', end='')

    print()

# Call main
main()
