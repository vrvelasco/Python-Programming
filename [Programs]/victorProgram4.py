# Victor Velasco (Program 4) 10/9/19

def main():
    # Variables
    total = 0
    scores = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
    TESTS = 7 # Constant

  # Get values
    for i in range(TESTS):
        tempScore = float(input('Enter the score for test # ' + (scores[i] + 1) + ': '))

        while tempScore < 0:
            tempScore = float(input('Enter a number greater than or equal to zero: '))

        scores[i] = tempScores
        
    # Calculate total
        # scores.sum()
    for test in scores:
        total += test
    
    # Calculate Average
        #scores.sum() / score.len() OR scores.sum() / TESTS
    calcAvg()

    # Display results
    print('\nScore' + 'Numeric Score'.center(45, ' '))
    print(''.ljust(26, '=')) # Formatting
    
    # Loop through list
    for s in scores:
       print('Score i + 1:' + format(i, '.1f').rjust(25, ' ')) 
    
    print(''.ljust(26, '=')) # Formatting
    print('Total:' + format(total, '.1f').rjust(25, ' '))
    print(''.ljust(26, '=')) # Formatting
    print('Average Score:' + format(average, '.1f').rjust(25, ' '))

def calcAvg():
    return average = total / TESTS
    
# Call main
main()
