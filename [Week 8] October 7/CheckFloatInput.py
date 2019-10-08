# Victor Velasco (Check Float Input) 10/7/19

num_str = input('Enter a float: ')

while True:
    try:
        num_float = float(num_str)
        break
    except ValueError:
        num_str = input('Error, enter a float: ')
print('Success:', num_float)
