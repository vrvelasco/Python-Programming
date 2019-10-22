# Victor Velasco (Character Analyzer) 10/21/2019

def main():
    # Variables
    num_upper = 0
    num_lower = 0
    num_space = 0
    num_digit = 0
    data = ''

    try:
        infile = open('text.txt', 'r')
        data = infile.read()

        for ch in data:
            if ch.isupper():
                num_upper += 1

            elif ch.islower():
                num_lower += 1

            elif ch.isdigit():
                num_digit += 1

            elif ch.isspace():
                num_space += 1
                
        infile.close()
        
        print('Upper case letters:', num_upper)
        print('Lower case letters:', num_lower)
        print('Digits:', num_digit)
        print('Spaces:', num_space)

    except IOError:
        print('There was an error while opening the file.')

    except:
        print('An error occurred.')

# Call main
main()
