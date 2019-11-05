# Victor Velasco (UniqueWords) 11/4/19

def main():
    # Get the name of the input file
    input_name = input('Enter the name of the input file: ')

    input_file = open(input_name, 'r')
    text = input_file.read()
    text_lower = text.lower()
    words = text_lower.split()

    # Create sets of unique words
    unique_words = set(words)
    print('These are the unique words in the text: ')
    for word in unique_words:
        print(word)
        
    input_file.close()

# Call main
main()
