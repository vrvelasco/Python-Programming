# Victor Velasco (Program 4) 10/9/19

def main():
    # Variables
    total = 0
    grades = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
    TESTS = 7 # Constant

    # Get values
    for i in range(TESTS):
        tempScore = float(input('Enter the score for test #' + str(i + 1) + ': '))

        while tempScore < 0:
            tempScore = float(input('Enter a number greater than or equal to zero: '))

        grades[i] = tempScore
        
    # Calculate total
        # grades.sum()
    for test in grades:
        total += test
    
    # Calculate Average
        #grades.sum() / grades.len()
        # grades.sum() / TESTS
    average = total / TESTS

    # Display results
    print('\nScore' + 'Numeric Score'.center(22, ' '))
    print(''.ljust(20, '=')) # Formatting
    
    # Loop through list
    for s in range(TESTS):
       print('Score ' + str(s + 1) + ':' + format(grades[s], '.1f').rjust(15, ' ')) 
    
    print(''.ljust(20, '=')) # Formatting
    print('Total:' + format(total, '.1f').rjust(18, ' '))
    print(''.ljust(20, '=')) # Formatting
    print('Average Score:' + format(average, '.1f').rjust(9, ' '))
    
# Call main
main()
