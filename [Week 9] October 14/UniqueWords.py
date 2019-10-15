# Victor Velasco (Unique Words) 10/14/19

def make_word(a_file):
    word_list = [] # Create list

    # First line
    for line_str in a_file:
        line_list = line_str.split()

        # First word without . or ,
        for word in line_list:
            word = word.lower()
            word = word.strip('.,')

            # Add word to list, if it's a word
            if word != "--":
                word_list.append(word)

    # Done
    return word_list

def make_unique(word_list):
    unique_list = [] # Create list

    # Get each word; find unique ones
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)

    return unique_list

gba_file = open('gettysburg.txt', 'r')

speech_list = make_word(gba_file)
unique_list = make_unique(speech_list)

print(unique_list)
print('Speech length: ', len(speech_list))
print('Unique length: ', len(unique_list))
