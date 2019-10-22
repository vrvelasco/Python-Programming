# Victor Velasco (Number of Words) 10/21/2019

# Variables
num_sentences = 0
total_words = 0
average_words = 0.0
words = []

try:
    infile = open('text.txt', 'r')
    sentences = infile.readlines()
    num_sentences = len(sentences)

    for item in sentences:
        words = item.split()
        total_words += len(words)

    average_words = float(total_words) / num_sentences
    print('The average number of words per line is:', average_words)

    infile.close()

except IOError:
    print('There was an error while opening the file.')

except:
    print('An error occurred.')
