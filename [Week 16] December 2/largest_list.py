# Victor Velasco (Largest List) 12/2/19

def main():
    MAX = 5 # Constant for size of the list
    number_list = []

    for i in range(MAX):
        user_num = int(input('Enter an integer between 1 and 100: '))

        while user_num < 1 or user_num > 100: # Check range
            user_num = int(input('Please try again: '))

        number_list.append(user_num)

        largest = find_largest(number_list)

    print('The largest number is:', largest)

def find_largest(num_list):
    n = len(num_list)

    if n == 1: # If the length is 1, then it's the only number in there
        return num_list[0]
    else:
        temp = find_largest(num_list[0:n - 1]) # [0:n-1] means goes from 0 to last element

        if num_list[n - 1] > temp: # Switch to '<' to find the smallest number instead
            return num_list[n - 1]
        else:
            return temp

# Call main
main()
