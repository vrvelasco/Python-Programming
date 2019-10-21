# Victor Velasco (Payroll) 9/9/19

hours_worked = float(input('Enter the hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))
ot_rate = float(input('Enter the overtime rate: '))

if hours_worked > 40:
    ot_hours = hours_worked -40
    reg_hours = 40.0
    reg_pay = reg_hours * pay_rate
    ot_pay = ot_rate * pay_rate * ot_hours
else:
    reg_hours = hours_worked
    reg_pay = reg_hours * pay_rate
    ot_pay = 0

total_pay = reg_pay + ot_pay

print('Total pay this period: $' + format(total_pay, ',.2f'))
