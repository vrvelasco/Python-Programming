# Victor Velasco (SumOfNumbers) 9/16/19

number = 1.0
total = 0.0

while number > 0:
    number = float(input('Enter a positive number'
                         '\nnegative to exit: '))
    if number > 0:
        total = total + number
print('Total =', format(total, ',.2f'))
