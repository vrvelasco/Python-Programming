# Victor Velasco (Manager Main) 11/25/19

import employee

def display_menu():
    print('***** Weekly Pay Calculator *****')
    print('Enter 1 for hourly employee')
    print('Enter 2 for salary employee')
    print('Enter 3 to exit')

def main():
    # Variables
    s_name = ''
    s_id = ''
    s_salary = 0.0
    s_bonus = 0.0

    w_name = ''
    w_id = ''
    w_shift = 0
    w_pay = 0.0
    w_hours = 0.0

    choice = 0

    display_menu()
    choice = int(input('Enter your choice: '))

    while choice != 3:
        if choice == 1:
            w_name = input('Enter the Employee Name: ')
            w_id = input('Enter the Employee ID: ')
            w_shift = int(input('Enter the Employee shift number: '))
            w_pay = float(input('Enter the Employee pay rate: '))
            w_hours = float(input('Enter the hours the Employee worked: '))

            worker = employee.ProductionWorker(w_name, w_id, w_shift, w_pay, w_hours)

            print('Production Worker Information')
            print('Name:', worker.get_name())
            print('ID Number:', worker.get_id_number())
            print('Shift Number:', worker.get_shift_number())
            print('Hourly Pay Rate: $', format(worker.get_pay_rate(), ',.2f'), sep='')
            print('Gross Weekly Pay: $', format(worker.get_weekly_pay(), ',.2f'), sep='')

        elif choice == 2:
            s_name = input('Enter the Name: ')
            s_id = input('Enter the ID Number: ')
            s_salary = float(input('Enter the Salary: '))
            s_bonus = float(input('Enter the Bonus Amount: '))

            supervisor = employee.ShiftSupervisor(s_name, s_id, s_salary, s_bonus)

            print('Shift Supervisor Information')
            print('Name:', supervisor.get_name())
            print('ID Number:', supervisor.get_id_number())
            print('Annual Salary: $', format(supervisor.get_salary(), ',.2f'), sep='')
            print('Bonus Amount: $', format(supervisor.get_bonus(), ',.2f'), sep='')
            print('Gross Weekly Pay: $', format(supervisor.get_weekly_pay(), ',.2f'), sep='')

        display_menu()
        choice = int(input('Enter your choice: '))

# Call main
main()
