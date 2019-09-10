# Victor Velasco (EvenOrOdd) 9/9/19

user_str = input('Enter a positive whole number: ')
my_int = int(user_str)

#Even or odd
if my_int % 2 == 0:
    print(my_int, 'is an even number.')
else:
    print(my_int, 'is an odd number.')

#
# Different example below (Biggest)
#

# Which is bigger
num1 = int(input('Enter the first whole number: '))
num2 = int(input('Enter the second whole number: '))
num3 = int(input('Enter the third whole number: '))
num4 = int(input('Enter the fourth whole number: '))

biggest = num1 # Holds it (For comparing)

if num2 > biggest:
    biggest = num2
if num3 > biggest:
    biggest = num3
if num4 > biggest:
    biggest = num4

print('The biggest number entered is:', biggest)
