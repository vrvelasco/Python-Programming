# Victor Velasco (Expense Pie Chart) 10/14/19

import matplotlib.pyplot as plt # Alias

def main():
    # Open file
    expense_file = open('expenses.txt', 'r')

    # Put in list
    expenses = expense_file.readlines()

    # Close file
    expense_file.close()

    for i in range(len(expenses)):
        expenses[i] = expenses[i].rstrip('\n') # Removes new line character

    slice_labels = [ 'Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc.' ]

    plt.pie(expenses, labels=slice_labels)
    plt.title('Monthly Expenses')
    plt.show()

# Call main
main()
