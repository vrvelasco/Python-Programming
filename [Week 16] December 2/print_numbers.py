# Victor Velasco (Print Numbers) 12/2/2019

def main():
    number = 0

    number = int(input('How many numbers should I display?: '))

    while number <= 0: # Check to see if it's in range
        number = int(input('Enter a number greater than zero: '))

    print_num(number)
    
def print_num(n):
    if n > 1:
        print_num(n - 1)

    print(n, sep=' ')

# Call main
main()
