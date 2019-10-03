# Victor Velasco (Program 3) 10/2/19

# Functions
def main():
    t1 = float(input('Please enter the FIRST test score: '))
    t2 = float(input('\nPlease enter the SECOND test score: '))
    t3 = float(input('\nPlease enter the THIRD test score: '))
    t4 = float(input('\nPlease enter the FOURTH test score: '))
    t5 = float(input('\nPlease enter the FIFTH test score: '))

    # Calculate Average
    average = calc_avg(t1, t2, t3, t4, t5)
    
    # Get Letter Grades
    g1 = get_grade(t1)
    g2 = get_grade(t2)
    g3 = get_grade(t3)
    g4 = get_grade(t4)
    g5 = get_grade(t5)
    
    # Display Results
    print('Score\tNumeric Score\tLetter Grade')
    print('Score 1:\t' + format(t1, ',.1f') + '\t' + g1)
    print('Score 2:\t' + format(t2, ',.1f') + '\t' + g2)
    print('Score 3:\t' + format(t3, ',.1f') + '\t' + g3)
    print('Score 4:\t' + format(t4, ',.1f') + '\t' + g4)
    print('Score 5:\t' + format(t5, ',.1f') + '\t' + g5)
    print('Average Score: \t')

def calc_avg(t1, t2, t3, t4, t5):
    calculated = (t1 * t2 * t3 * t4 * t5) / 5
    return calculated

def get_grade(t):
    if average >= 90:
        letterGrade = 'A'
    elif average >= 80 and average <= 89:
        letterGrade = 'B'
    elif average >= 70 and average <= 79:
        letterGrade = 'C'
    elif average >= 60 and average <= 69:
        letterGrade = 'D'
    else: 
        letterGrade = 'F'
    return letterGrade
    
# Call main
main()
