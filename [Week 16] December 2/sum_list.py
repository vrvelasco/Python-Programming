# Victor Velasco (Sum List) 12/2/19

def main():
    MAX = 5 # Constant for size of the list
    number_list = []

    for i in range(MAX):
        user_num = int(input('Enter an integer between 1 and 100: '))

        while user_num < 1 or user_num > 100: # Check range
            user_num = int(input('Please try again: '))

        number_list.append(user_num)

    # Print list
    print('List of numbers:\n', number_list, sep=' ')

    sum = sum_list(number_list)

    print('Sum of all of the numbers is:', sum)

def sum_list(num_list):
    n = len(num_list)

    if len(num_list) ==1:
        return num_list[0]
    else:
        return num_list[n - 1] + sum_list(num_list[0:n - 1])

# Call main
main()
