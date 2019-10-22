# Victor Velasco (Most and Least Common) 10/21/2019

# Variables
LOTTERY_NUMBERS = 69 # Constant

def get_all_numbers():
    pblottery_file = open('pbnumbers.txt', 'r')
    pblottery = pblottery_file.readlines()

    pblottery_file.close()

    for i in range(len(pblottery)):
        pblottery[i] = pblottery[i].rstrip('\n')

    lotto_nums = []

    for i in range(len(pblottery)):
        number_set = pblottery[i].split()

        for j in range(len(number_set)):
            lotto_nums.append(int(number_set[j]))

    return lotto_nums

def get_frequency(number_list, max_value):
    frequency = [0] * (max_value + 1)

    for i in range(len(number_list)):
        num = number_list[i]
        frequency[num] += 1

    return frequency

def position_of_highest_value(num_list):
    highest = 0
    highest_position = 0

    for i in range(len(num_list)):
        if num_list[i] > highest:
            highest = num_list[i]
            highest_position = i

    return highest_position

def most_common(freq_list):
    common_sorted = []
    temp_list = []

    for item in freq_list:
        temp_list.append(item)

    for i in range(len(temp_list)):
        position = position_of_highest_value(temp_list)
        common_sorted.append(position)
        temp_list[position] = -1

    return common_sorted

def main():
    lotto_nums = get_all_numbers()
    frequency = get_frequency(lotto_nums, LOTTERY_NUMBERS)
    sorted_by_most_common = most_common(frequency)
    
    # Display
    print('10 Most Common Numbers (Highest to Lowest)')
    print('------------------------------------------')

    for i in range(10):
        print(sorted_by_most_common[i])

    sorted_by_most_common.reverse()
    print('\n10 Least Common Numbers (Lowest to Highest)')
    print('-------------------------------------------')

    for i in range(1, 11):
        print(sorted_by_most_common[i])

# Call main
main()
