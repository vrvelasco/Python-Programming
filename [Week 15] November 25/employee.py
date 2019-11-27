# Victor Velasco (employee) 11/25/19

class Employee:
    # Constructor
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    # Getters
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number
        
    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_id_number(self, id_number):
        self.__id_number = id_number

class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate, hours_worked):
        Employee.__init__(self, name, id_number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate
        self.__hours_worked = hours_worked

    # Setters
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    # Getters
    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate

    def get_hours_worked(self):
        return self.__hours_worked

    def get_weekly_pay(self):
        HOURS = 40.0
        OT_RATE = 2.0

        if self.__hours_worked > HOURS:
            reg_pay = HOURS *self.__pay_rate
            ot_pay = (self.__hours_worked - HOURS) * OT_RATE * self.__pay_rate
            pay = reg_pay + ot_pay
            
        else:
            pay = self.__hours_worked * self.__pay_rate

        return pay

class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, salary, bonus):
        Employee.__init__(self, name, id_number)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

    def get_weekly_pay(self):
        NO_WEEKS = 52
        total_comp = self.__salary + self.__bonus
        pay = total_comp / NO_WEEKS

        return pay
