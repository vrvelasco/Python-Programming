# Victor Velasco (Text Files) 10/14/19

def main():
    team = ''
    win_count = 0

    try:
        input_file = open('WorldSeriesWinners.txt', 'r')
        winners = input_file.readlines()

        for i in range(len(winners)):
            winners[i] = winners[i].rstrip('\n')

        team = input('Enter the name of a team: ')
        if team not in winners:
            print('The', team, 'have never won the World Series.')
        else:
            for item in winners:
                if item == team:
                    win_count += 1

            print('The', team, 'won the World Series', win_count, 'times between 1903 and 2018.')

    except IOError:
        print('The file could not be found.')

    except IndexError:
        print('There was an indexing error.')

    except:
        print('An error occurred.')

# Call main
main()
