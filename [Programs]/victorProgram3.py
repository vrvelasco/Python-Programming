# Victor Velasco (Program 3) 10/2/19

# Functions
def main():
    t1 = float(input('Please enter the FIRST test score: '))
    t2 = float(input('Please enter the SECOND test score: '))
    t3 = float(input('Please enter the THIRD test score: '))
    t4 = float(input('Please enter the FOURTH test score: '))
    t5 = float(input('Please enter the FIFTH test score: '))

    # Calculate Average
    average = calc_avg(t1, t2, t3, t4, t5)
    
    # Get Letter Grades
    g1 = get_grade(t1)
    g2 = get_grade(t2)
    g3 = get_grade(t3)
    g4 = get_grade(t4)
    g5 = get_grade(t5)
    
    # Display Results
    print('\nScore' + 'Numeric Score'.center(25, ' ') + 'Letter Grade')
    print(''.ljust(26, '=')) # Formatting
    print('Score 1:' + format(t1, '.1f').rjust(15, ' ') + g1.rjust(25, ' '))
    print('Score 2:' + format(t2, '.1f').rjust(15, ' ') + g2.rjust(25, ' '))
    print('Score 3:' + format(t3, '.1f').rjust(15, ' ') + g3.rjust(25, ' '))
    print('Score 4:' + format(t4, '.1f').rjust(15, ' ') + g4.rjust(25, ' '))
    print('Score 5:' + format(t5, '.1f').rjust(15, ' ') + g5.rjust(25, ' '))
    print(''.ljust(40, '-')) # Formatting
    print('Average Score:'.ljust(40, ' ') + format(average, '.1f'))

def calc_avg(t1, t2, t3, t4, t5):
    calculated = (t1 + t2 + t3 + t4 + t5) / 5
    return calculated

def get_grade(t):
    if t >= 90:
        letterGrade = 'A'
    elif t >= 80 and t <= 89:
        letterGrade = 'B'
    elif t >= 70 and t <= 79:
        letterGrade = 'C'
    elif t >= 60 and t <= 69:
        letterGrade = 'D'
    else: 
        letterGrade = 'F'
    return letterGrade
    
# Call main
main()
