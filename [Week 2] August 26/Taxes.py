# Victor Velasco 8/26/19

# Variables
purchase = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0
totalSale = 0.0
STATE_TAX = 0.07
COUNTY_TAX = 0.0225

purchase = float(input("Enter the amount of the purchase: "))
stateTax = STATE_TAX * purchase
countyTax = COUNTY_TAX * purchase
totalTax = stateTax + countyTax
totalSale = purchase + totalTax

# Display
print("Purchase Amount: $" + format(purchase, ',.2f'))
print("State Tax:             $" + format(stateTax, ',.2f'))
print("County Tax:          $" + format(countyTax, ',.2f'))
print("Total Tax:             $" + format(totalTax, ',.2f'))
print("Total Sale: $" + format(totalSale, ',.2f'))
