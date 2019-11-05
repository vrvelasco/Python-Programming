# Victor Velasco (Course Information) 11/4/19

def main():
    # Dictionaries
    rooms = { 'CIS 187 001' : 2158, 'CIS 165 001' : 2157, 'CIS 185 001' : 2159,
              'CIS 195 001' : 2152, 'CIS 164 001' : 2158 }
    instructors = { 'CIS 187 001' : 'Helen Thomas', 'CIS 165 001' : 'Helen Thomas',
                    'CIS 185 001' : 'Lawrence Appelbaum', 'CIS 195 001' : 'Lawrence Appelbaum', 'CIS 164 001' : 'Nikki Hensley' }
    time = { 'CIS 187 001' : '2:00PM', 'CIS 165 001' : '6:00PM', 'CIS 185 001' : '9:00AM', 'CIS 195 001' : '2:00PM',
             'CIS 164 001' : '11:00AM' }
    days = { 'CIS 187 001' : 'Monday and Wednesday', 'CIS 165 001' : 'Monday',
             'CIS 185 001' : 'Monday and Wednesday', 'CIS 195 001' : 'Monday and Wednesday',
             'CIS 164 001' : 'Tuesday and Thursday' }

    # Get course number from the user
    course = input('Enter a course number: ')

    if course not in rooms:
        print(course, 'is an invalid course number.')
    else:
        print('The details for course', course, 'are:')
        print('IS Building Room:', rooms[course])
        print('Instructor:', instructors[course])
        print('Time:', time[course])
        print('Day:', days[course])

# Call main
main()
