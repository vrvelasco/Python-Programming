# Victor Velasco (Exponents) 12/2/19

# Global
MIN = 1
MAX = 100

def main():
    # Local
    num = 0.0
    exp = 0

    num = float(input('Enter a number: '))

    while exp < MIN or exp > MAX:
        exp = int(input('Enter a positive whole number between ' + str(MIN) + ' and ' + str(MAX) + ': '))

    print(num, 'raised to the power of', exp, 'is', format(power(num, exp), ',.2f'))

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

# Call main
main()
