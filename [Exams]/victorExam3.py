# Victor Velasco (Exam 3) 12/2/19

def main():
    MAX = 10 # Constant for size of the list
    userNum = 0 # Number from the user
    numberList = [] # Holds numbers
    choice = 0 # User's menu option
    name = {1:'First', 2:'Second', 3:'Third', 4:'Fourth', 5:'Fifth', 6:'Sixth', \
                  7:'Seventh', 8:'Eighth', 9:'Ninth', 10:'Tenth'} # Formatting

    # Intro
    print('Welcome!\n\nYou will be working with a list of ten numbers. Please enter them below.\n') 
    
    # Get ten numbers
    for i in range(MAX):
        print(name[i + 1], 'number', end='')
        try: # Try to get a valid integer from the user
            userNum = int(input(' ► Enter an integer between 1 and 100: '))
        except:
            userNum = -1 # Error
        
        # Check range of number
        while userNum < 1 or userNum > 100: 
            try: # Try to get a valid integer from the user
                userNum = int(input('\nInvalid integer. Please try again: '))
            except:
                userNum = -1 # Error

        numberList.append(userNum) # Add the number to the list

    # Loop while the user doesn't want to exit
    while choice != 4:
        # Print list
        print('\n\tList of numbers:', numberList,'\n', sep=' ')
            
        # Display the menu and get the user's choice
        choice = displayMenu()

        # Match choice to menu options
        if choice == 1:
            largest = find_largest(numberList)
            print('The largest number is:', largest)
        elif choice == 2:
            smallest = find_smallest(numberList)
            print('The smallest number is:', smallest)
        elif choice == 3:
            result = sumList(numberList)
            print('The sum of all of the numbers is:', result)

    print('\nGoodbye!')
def displayMenu():
    # Menu options
    print('*** MENU ***')
    print('Enter 1 to find the largest number')
    print('Enter 2 to find the smallest number')
    print('Enter 3 to sum the list of numbers')
    print('Enter 4 to exit')

    # Try to get a valid choice from the user
    try:
        selection = int(input('Selection: ')) 
    except:
        selection = -1 # Error

    # Verify that the selection is in range
    while selection < 1 or selection > 4:
        try:
            selection = int(input('\nInvalid selection. Please try again: ')) 
        except:
            selection = -1 # Error

    # Return the option selected now that it's correct
    return selection

def findLargest(numList):
    n = len(numList)

    if n == 1: # If the length is 1, then it's the only number in there
        return numList[0]
    else:
        temp = findLargest(numList[0:n - 1]) # [0:n-1] means goes from 0 to last element

        if numList[n - 1] > temp: 
            return numList[n - 1]
        else:
            return temp

def findSmallest(numList):
    n = len(numList)

    if n == 1: # If the length is 1, then it's the only number in there
        return numList[0]
    else:
        temp = findSmallest(numList[0:n - 1]) # [0:n-1] means goes from 0 to last element

        if numList[n - 1] < temp: 
            return numList[n - 1]
        else:
            return temp
        
def sumList(numList):
    n = len(numList)

    if len(numList) ==1:
        return numList[0]
    else:
        return numList[n - 1] + sumList(numList[0:n - 1])

# Call main
main()
