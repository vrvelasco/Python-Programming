# Victor Velasco (Exam 2) 10/22/19

def main():
    choice = displayMenu()
    
    while choice != 5: # Did the user select to exit?
        # Get the user's input
        user_string = input('\nPlease enter a string: ')
    
        # Validate the string is not empty
        while len(user_string) == 0:
            user_string = input('\nPlease enter at least one character: ')
        
        # Go through different options        
        if choice == 1: # Uppercase
            upperStr = user_string.upper()
            formatted(user_string, upperStr)  
            
        elif choice == 2: # Lowercase
            lowerStr = user_string.lower()
            formatted(user_string, lowerStr)
            
        elif choice == 3: # Number of words
            # Split words on spaces
            user_list = user_string.split()
            
            # Counted words
            words = '{} word(s) were found in the string.'.format(len(user_list))
            formatted(user_string, words)  
            
        elif choice == 4: # Number of vowels
            number = vowel_counter(user_string) # Counts vowels
            
            result = '{} vowel(s) were found in the string.'.format(number)
            formatted(user_string, result)         

        choice = displayMenu()
    print('\nGoodbye!')
    
def displayMenu():
    choice = int(input('\n╔═══════════════════════════════════════════════════╗' + 
                       '\n║                     MAIN MENU                     ║' + 
                       '\n╠═══════════════════════════════════════════════════╣' +
                       '\n║ Enter 1 to convert a string to uppercase          ║' +
                       '\n║ Enter 2 to convert a string to lowercase          ║' +
                       '\n║ Enter 3 to count the number of words in a string  ║' +
                       '\n║ Enter 4 to count the number of vowels in a string ║' +
                       '\n║ Enter 5 to exit                                   ║' +
                       '\n╚═══════════════════════════════════════════════════╝\nSelection: '))


    # Test input is in the correct range
    while choice < 1 or choice > 5:
        choice = int(input('\nInvalid selection. Please try again: '))
    
    return choice
    
def formatted(original, changed):
    print('\nOriginal string: {}\nResult: {}'.format(original, changed))
    
def vowel_counter(string):
    count = 0
    vowels = 'aeiou'

    for ch in string.lower():
        if vowels.find(ch) >= 0:
            count += 1

    return count
    
# Call main
main()
