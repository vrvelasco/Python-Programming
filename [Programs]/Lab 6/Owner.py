# Victor Velasco (Owner) 12/1/19

class Customer:
    # Constructor
    def __init__(self, name, address, phone_number, email):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__email = email
        
    # Setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_email(self, email):
        self.__email = email
        
    #Getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email
    
class Pet:
    # Constructor
    def __init__(self, pet_name, pet_type, pet_age):
        self.__pet_name = pet_name
        self.__pet_type = pet_type
        self.__pet_age = pet_age
        
    # Setters
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def set_pet_age(self, pet_age):
        self.__pet_age = pet_age
        
    # Getters
    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    def get_pet_age(self):
        return self.__pet_age

class Invoice:
    # Constructor
    def __init__(self, charges, tax):
        self.__charges = charges
        self.__tax = tax

    # Setters
    def set_charges(self, charges):
        self.__charges = charges

    def set_tax(self, tax):
        self.__tax = tax

    # Getters
    def get_charges(self):
        return self.__charges

    def get_tax(self):
        return self.get_charges() * self.__tax

    def get_total(self):
        return self.get_charges() + self.get_tax()
