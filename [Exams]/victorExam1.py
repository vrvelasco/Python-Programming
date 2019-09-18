# Victor Velasco (Exam 1) 9/16/19

# Variables
pay = 0.0
total = 0.0
sales = 0.0
average = 0.0
days = 1

# Input
sales = float(input('Please enter the number of daily sales: '))
total +=sales

# Math
average = sales / days
pay = total * .10


# Output
print('\nAverage Sales: $' + format(average, ',.2f'))
print('Total Sales:       $' + format(total, ',.2f'))
print('Pay:                    $' + format(pay, ',.2f'))
