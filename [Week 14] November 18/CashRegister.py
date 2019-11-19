# Victor Velasco (Cash Register) 11/18/19

import Retail

class CashRegister:
    
    def __init__(self):
        self.__items = []

    def clear(self):
        self.__items = []

    def purchase_item(self, retail_item):
        self.__items.append(retail_item)
        print('The item was added to the cash register.')
        
    def get_total(self):
        total = 0.0

        for item in self.__items:
            total += item.get_price()

        return total

    def show_items(self):
        print('The items in the cash register are:')
        print() # Blank line

        for item in self.__items:
            print(item.get_description())
            print() # Blank line
            
