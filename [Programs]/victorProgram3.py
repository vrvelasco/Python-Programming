# Victor Velasco (Program 3) 10/2/19

# Functions
def main():
    
def calc_avg(t1, t2, t3, t4, t5):
    average = (t1 * t2 * t3 * t4 * t5) / 5
    return average

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
        letterGrade = 'F'\
    return letterGrade
    
# Call main
main()
