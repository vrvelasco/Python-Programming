# Victor Velasco (SoftwareSales) 9/9/19

RETAIL_PRICE = 99.0

qnty = int(input('Enter the quantity of software: '))

if qnty > 99:
    disc_rate = 0.140
elif qnty > 49:
    disc_rate = 0.30
elif qnty > 19:
    disc_rate = 0.20
elif qnty > 9:
    disc_rate = 0.10
else:
    disc_rate = 0.0

disc_amount = disc_rate * RETAIL_PRICE
disc_price = RETAIL_PRICE - disc_amount
total = disc_price * qnty

print('Your Price: $' + format(disc_price, ',.2f') + '\nTotal Cost: $' + format(
    total, ',.2f'))
