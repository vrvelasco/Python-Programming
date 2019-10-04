# Victor Velasco (AreaFunctions) 9/30/19

import math

# Functions (Methods)
def displayMenu():
    print('*** Shape Area Calculator ***')
    print('Enter 1 for a Square')
    print('Enter 2 for a Rectangle')
    print('Enter 3 for a Circle')
    print('Enter 4 for a Triangle')
    print('Enter 5 to exit')

def square():
    side = float(input('Enter the measurement of the side: '))
    while side <= 0:
        side = float(input('Enter a positive number: '))
    area = side**2
    print('Area of the square is:', format(area, ',.2f'))

def rectangle():
    length = float(input('Enter the measurement of the length: '))
    while length <= 0:
        length = float(input('Enter a positive number: '))
    width = float(input('Enter the measurement of the width: '))
    while width <= 0:
        width = float(input('Enter a positive number: '))
    area = length * width
    print('Area of the rectangle is:', format(area, ',.2f'))

def circle():
    radius = float(input('Enter the measurement of the radius: '))
    while radius <= 0:
        radius = float(input('Enter a positive number: '))
    area = math.pi * radius**2
    print('Area of the circle is:', format(area, ',.2f'))
    
def triangle():
    base = float(input('Enter the measurement of the base: '))
    while base <= 0:
        base = float(input('Enter a positive number: '))
    height = float(input('Enter the measurement of the height: '))
    while height <= 0:
        height = float(input('Enter a positive number: '))
    area = .5 * base * height
    print('Area of the triangle is:', format(area, ',.2f'))
