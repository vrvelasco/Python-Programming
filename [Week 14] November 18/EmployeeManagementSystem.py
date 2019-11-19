# Victor Velasco (Employee Management System) 11/18/19

import Employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
PRINT = 5
QUIT = 6

FILENAME = 'employees.dat'

def main():
    employees = load_employee()

    choice = 0

    while choice != QUIT:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)
        elif choice == PRINT:
            print_emp(employees)
        
    save_employees(employees)

def load_employee():
    try:
        input_file = open(FILENAME, 'rb')
        employee_dict = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dict = {}

    return employee_dict

def get_user_choice():
    print('Enter 1 to Look up an employee')
    print('Enter 2 to Add a new employee')
    print('Enter 3 to Change an existing employee')
    print('Enter 4 to Delete an employee')
    print('Enter 5 to Print employee list')
    print('Enter 6 to Quit the program')
    employees = load_employee()
    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a number between 1 and 6.'))

    return choice

def look_up(employees):
    ID = input('Enter an employee ID number: ')

    print(employees.get(ID, 'The specified ID number was not found.'))

def add(employees):
    name = input("Enter the employee's name: ")
    ID = input("Enter the employee's ID number: ")
    department = input("Enter the employee's department: ")
    title = input("Enter the employee's title: ")

    new_emp = employee.Employee(name, ID, department, title)

    if ID not in employees:
        employees[ID] = new_emp
        print('The employee has been added.')
    else:
        print('An employee with that ID already exists.')

def change(employees):
    ID = input('Enter employee ID number: ')

    if ID in employees:
        name = input('Enter the new name: ')
        department = input('Enter the new department: ')
        title = input('Enter the new title: ')


        new_emp = employee.Employee(name, ID, department, title)
        employees[ID] = new_emp
        print('Employee information updated.')
    else:
        print('The specified ID number was not found.')

def delete(employees):
    ID = input('Enter the employee ID number: ')

    if ID in employees:
        del employees[ID]
        print('Employee information deleted')
    else:
        print('The specified ID number was not found.')

def print_emp(employees):
    for ID in employees:
        print(employees.get(ID))

def save_employees(employees):
    output_file = open(FILENAME, 'wb')

    pickle.dump(employees, output_file)
    output_file.close()

# Call main
main()
