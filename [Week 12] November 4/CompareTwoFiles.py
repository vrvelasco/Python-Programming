# Victor Velasco (Compare Two Files) 11/4/19

def main():
    # Get first file and find unique words
    file1 = open('text.txt', 'r')
    text1 = file1.read()
    text1_lower = text1.lower()
    file1.close()
    words1 = text1_lower.split()
    set1 = set(words1)

    # Get second file and find unique words
    file2 = open('words.txt', 'r')
    text2 = file2.read()
    text2_lower = text2.lower()
    file2.close()
    words2 = text2_lower.split()
    set2 = set(words2)

    # Union
    union = set1.union(set2)
    print('These are the unique words that are contained in both files: ')
    for item in union:
        print(item)
    print() # Empty line after For loop

    # Intersection
    intersection = set1.intersection(set2)
    print('These are the words that appear in both files: ')
    for item in intersection:
        print(item)
    print()

    # Difference
    difference1 = set1.difference(set2)
    print('These are the words that appear in the first file, but do not appear in the second file:')
    for item in difference1:
        print(item)
    print()

    # Symmetrical Difference
    sym_diff = set1.symmetric_difference(set2)
    print('These are the words that appear in the first file or the second file, but do not appear in the both of the files: ')
    for item in sym_diff:
        print(item)
    print()
    
# Call main
main()
