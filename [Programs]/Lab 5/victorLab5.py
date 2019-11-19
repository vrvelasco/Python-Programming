# Victor Velasco (Lab 5)

def main():
    print('LAB 5 » This program compare any two text files.')
    # Display the menu to the user and get a selection from them
    option = menu()
    
    # Verify the choice is in range
    while option < 1 or option > 6:
        print('\nINVALID SELECTION » Please try again.')
        option = menu()
        
    # Check to see if the user wants to exit
    while option != 6:
        # Go through the different options
        if option == 1: # Unique words
            s1, s2 = processor()
            if s1 != None or s2 != None:
                union(s1, s2)
        elif option == 2: # Words that appear in both files
            s1, s2 = processor()
            if s1 != None or s2 != None:
                intersection(s1, s2)
        elif option == 3: # Words that only appear in the first file
            s1, s2 = processor()
            if s1 != None or s2 != None:
                difference(s1, s2)
        elif option == 4: # Words that only appear in the second file
            s1, s2 = processor()
            if s1 != None or s2 != None:
                difference(s2, s1)
        elif option == 5: # Unique words in either the first or second files, but not in both
            s1, s2 = processor()
            if s1 != None or s2 != None:
                sym_diff(s1, s2)

        # Display menu again
        option = menu()
        
        # Verify the choice is in range
        while option < 1 or option > 6:
            print('\nINVALID SELECTION » Please try again.')
            option = menu()

    print('\nGoodbye!')
        
def menu():
    try: # Try to get a choice from the user
        choice = int(input('\nMAIN MENU: Select an option below to continue... \n' +
            '══════════════════════════════════════════════════════════════════════════════════════\n' +               
            '● Enter 1 to display the unique words\n' +
            '● Enter 2 to display the words that appear in both files\n' +
            '● Enter 3 to display the words that only appear in the first file\n' +
            '● Enter 4 to display the words that only appear in the second file\n' +
            '● Enter 5 to display unique words in either the first or second files but not in both\n' +
            '● Enter 6 to exit the program\n' +
            '══════════════════════════════════════════════════════════════════════════════════════\n' +
            'Selection: '))
    except:
        choice = -1 # Error
    return choice
    
def processor():
    # Get the file names
    f1 = input('\n\nPlease enter the name of the first file including the extention: ')
    f2 = input('Please enter the name of the second file including the extention: ')

    try: # Try to open the file given by user
        # Get first file and find unique words
        file1 = open(f1, 'r')
        text1 = file1.read()
        text1_lower = text1.lower()
        file1.close()
        words1 = text1_lower.split()
        set1 = set(words1)

        # Get second file and find unique words
        file2 = open(f2, 'r')
        text2 = file2.read()
        text2_lower = text2.lower()
        file2.close()
        words2 = text2_lower.split()
        set2 = set(words2)

        return set1, set2
    
    except:
        print('\nERROR » An error occurred opening the file(s). Please try again.')
        
        return None, None # Error
    
def union(set1, set2):
    # Union
    union = set1.union(set2)
    for item in union:
        print(item)
    print() # Empty line after For loop

def intersection(set1, set2):
    # Intersection
    intersection = set1.intersection(set2)
    for item in intersection:
        print(item)
    print() # Empty line after For loop

def difference(set1, set2):
    # Difference
    difference1 = set1.difference(set2)
    for item in difference1:
        print(item)
    print() # Empty line after For loop

def sym_diff(set1, set2):
    # Symmetrical Difference
    sym_diff = set1.symmetric_difference(set2)
    for item in sym_diff:
        print(item)
    print() # Empty line after For loop
    
# Call main
main()
