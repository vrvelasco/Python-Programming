# Victor Velasco (Word Separator) 10/21/2019

def main():
    result = ''
    user_string = input('Enter a string: ')

    result = result + user_string[0]

    for i in range(1, len(user_string)):
        ch = user_string[i]

        if ch.isupper():
            ch = ch.lower()
            result = result + ' '

        result = result + ch

    print(result)

main()
