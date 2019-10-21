# Victor Velasco (Program 4) 10/9/19

def main():
    # Variables
    total = 0
    scores = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
    TESTS = 7 # Constant

    # Get values
    for i in range(TESTS):
        tempScore = float(input('Enter the score for test #' + str(i + 1) + ': '))

        while tempScore < 0:
            tempScore = float(input('Enter a number greater than or equal to zero: '))

        scores[i] = tempScore
        
    # Calculate total
        # scores.sum()
    for test in scores:
        total += test
    
    # Calculate Average
        #scores.sum() / score.len() OR scores.sum() / TESTS
    average = total / TESTS

    # Display results
    print('\nScore' + 'Numeric Score'.center(29, ' '))
    print(''.ljust(26, '=')) # Formatting
    
    # Loop through list
    for s in range(TESTS):
       print('Score ' + str(s + 1) + ':' + format(scores[s], '.1f').rjust(18, ' ')) 
    
    print(''.ljust(26, '=')) # Formatting
    print('Total:' + format(total, '.1f').rjust(20, ' '))
    print(''.ljust(26, '=')) # Formatting
    print('Average Score:' + format(average, '.1f').rjust(12, ' '))
    
# Call main
main()
