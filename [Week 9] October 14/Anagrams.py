# Victor Velasco (Anagrams) 10/14/19

def are_anagrams(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    if word1_sorted == word2_sorted:
        return True
    else:
        return False

two_words = input('Enter two words, seperated by a space: ')
two_words_list = two_words.split() # Create list

# Put words in variables
word1 = two_words_list[0]
word2 = two_words_list[1]

# Test words
if are_anagrams(word1, word2):
    print('The words are anagrams.')
else:
    print('The words are not anagrams.')
