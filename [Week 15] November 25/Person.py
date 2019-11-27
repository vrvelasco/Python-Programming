# Victor Velasco (Person) 11/25/19

class Person:
    # Constructor
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        
    # Setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    #Getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    
class Customer(Person):
    # Constructor
    def __init__(self, name, address, phone_number, cust_number, on_list):
        Person.__init__(self, name, address, phone_number)
        self.__cust_number = cust_number
        self.__on_list = on_list

    # Setters
    def set_cust_number(self, cust_number):
        self.__cust_number = cust_number

    def set_on_list(self, on_list):
        self.__on_list = on_list
        
    # Getters
    def get_cust_number(self):
        return self.__cust_number

    def get_on_list(self):
        return self.__on_list
