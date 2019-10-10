# Victor Velasco (Program 4) 10/9/19

def main():
    # Variables
    total = 0
    TESTS = 7 # Constant

  # Get user input
    t1 = float(input('Please enter the FIRST test score: '))
    t2 = float(input('Please enter the SECOND test score: '))
    t3 = float(input('Please enter the THIRD test score: '))
    t4 = float(input('Please enter the FOURTH test score: '))
    t5 = float(input('Please enter the FIFTH test score: '))
    t6 = float(input('Please enter the SIXTH test score: '))
    t7 = float(input('Please enter the SEVENTH test score: '))

    # Add to list
    grades = [ t1, t2, t3, t4, t5, t6, t7 ] 

    # Calculate total
    for test in grades:
        total += test
    
    # Calculate Average
    average = calc_avg(t1, t2, t3, t4, t5)

    # Display results
    print('\nScore' + 'Numeric Score'.center(45, ' '))
    print(''.ljust(26, '=')) # Formatting
    print('Score 1:' + format(t1, '.1f').rjust(25, ' '))
    print('Score 2:' + format(t2, '.1f').rjust(25, ' '))
    print('Score 3:' + format(t3, '.1f').rjust(25, ' '))
    print('Score 4:' + format(t4, '.1f').rjust(25, ' '))
    print('Score 5:' + format(t5, '.1f').rjust(25, ' '))
    print('Score 6:' + format(t6, '.1f').rjust(25, ' '))
    print('Score 7:' + format(t7, '.1f').rjust(25, ' '))
    print(''.ljust(26, '=')) # Formatting
    print('Total:' + format(total, '.1f').rjust(25, ' '))
    print(''.ljust(26, '=')) # Formatting
    print('Average Score:' + format(average, '.1f').rjust(25, ' '))

def calc_avg(t1, t2, t3, t4, t5):
    calculated = (t1 + t2 + t3 + t4 + t5) / 5
    return calculated
    
# Call main
main()