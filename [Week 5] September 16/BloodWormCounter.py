# Victor Velasco (BloodWormCounter) 9/16/19

# Variables
PRICE = 0.33 # Constant for worm price
days = 0
worms = 0
total = 0.0
cost = 0.0
counter = 0
average = 0.0

days = int(input('Number of days: '))

while days <= 0:
    days = int(input('Days must be greater than zero: '))

# Get number of worms collected
for i in range(counter, days, 1):
    worms = int(input('Enter the number of worms collected: '))
    while worms <= 0:
        worms = int(input('You must enter the number of worms collected: '))
    total += worms

# Math
cost = total * PRICE
average = cost / days

print('Total Worms Collected:', total)
print('Total Cost:', format(cost, ',.2f'), sep = '', end = '\n')
print('Daily Average:', format(average, ',.2f'))
