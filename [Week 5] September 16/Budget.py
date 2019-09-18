# Victor Velasco (Budget) 9/16/19

budget = 0.0
difference = 0.0
total = 0.0
spent = 1.0

budget = float(input('Enter amount bugeted for the month: '))

while budget < 0:
    budget = float(input('Incorrect entry, must be greater than zero.'))

while spent != 0:
    spent = float(input('Enter amount spent or zero to exit: '))
    total += spent

print('Budgeted Amount: $' + format(budget, ',.2f'))
print('Total Expenses:  $' + format(total, ',.2f'))

if budget > total:
    difference = budget - total
    print('You are $' + format(difference, ',.2f') + ' under budget')
elif budget < total:
    difference = total - budget
    print('You are $' + format(difference, ',.2f') + ' over budget.')
else:
    print('Spending matches your budget.')
