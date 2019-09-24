# Victor Velasco (Exam 1) 9/16/19

# Variables
pay = 0.0
total = 0.0
sales = 0.0
average = 0.0
days = 0
counter = 0

# Get days
days = int(input('Please enter the number of day(s): '))
#To prevent a divide by zero error we need to prevent the user from entering 0.
while days <= 0:
    days = int(input('Incorrect entry.\nPlease try again.\n'))

print() # Formatting - Adds blank line

# Get sales
for i in range(counter, days, 1):
    sales = float(input(f'Please enter day {i + 1} sales amount: ')) # Formatting - Displays the day number
    #We can also prevent zero for sales.
    while sales <= 0:
        sales = float(input('Incorrect entry.\nPlease try again.\n'))
    total += sales

# Math
average = total / days
pay = total * .10

# Output
print('\nAverage Sales: $' + format(average, ',.2f'))
print('Total Sales:   $' + format(total, ',.2f'))
print('Pay:           $' + format(pay, ',.2f'))
