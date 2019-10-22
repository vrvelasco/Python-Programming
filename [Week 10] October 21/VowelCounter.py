# Victor Velasco (Vowel Counter) 10/21/2019

def main():
    # Variables
    vowels = 0
    consonants = 0
    user_string = input('Enter a string:').lower()

    vowels = vowel_counter(user_string)
    consonants = consonant_counter(user_string)

    print('\nThe string you entered includes {} vowels and {} consonants.'.format(vowels, consonants))

def vowel_counter(string):
    count = 0
    vowels = 'aeiou'

    for ch in string:
        if vowels.find(ch) >= 0:
            count += 1

    return count

def consonant_counter(string):
    count = 0
    consonants = 'bcdfghjklmnpqrstvwxyz'

    for ch in string:
        if consonants.find(ch) >= 0:
            count += 1

    return count

# Call main
main()
