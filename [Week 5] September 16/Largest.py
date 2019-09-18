# Victor Velasco (Largest) 9/16/19

largest = 0
counter = int(input('How many numbers do you want to check?'))

while counter <= 0:
    int(input('You must enter a number greater than zero: '))

for i in range(counter):
    
    number = int(input('Enter a number greater than zero and less than 101.'))

    while number < 1 or number > 100:
        number = int(input('You must enter a number greater than zero and less than 101.'))

    if number > largest:
        largest = number

print('The largest number is: ', largest)
