# Victor Velasco (Average Sales) 10/14/19

def main():
    # Variables
    total_sales = 0.0
    daily_sales = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
    days_of_week = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ]

    # Get values
    for i in range(7):
        todays_sales = float(input('Enter the sale for ' + days_of_week[i] + ': '))

        while todays_sales < 0:
            todays_sales = float(input('Enter a number greater than or equal to zero: '))

        daily_sales[i] = todays_sales

    # Get sum
    for number in daily_sales:
        total_sales += number

    print('\nTotal sales for the week: $' + format(total_sales, ',.2f'), sep='')

# Call main
main()
