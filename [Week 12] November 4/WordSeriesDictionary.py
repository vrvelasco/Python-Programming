# Victor Velasco (Word Series Dictionary) 11/4/19

BASE_YEAR = 1903

def main():
    # Variables
    year_dict = {}
    count_dict = {}

    input_file = open('WorldSeriesWinners.txt', 'r')
    winners = input_file.readlines()

    for i in range(len(winners)):
        team = winners[i].rstrip('\n')
        year = BASE_YEAR + i

        if year >= 1904: # Skips this year
            year +=1

        if year >= 1994: # This one too
            year +=1

        year_dict[str(year)] = team

        if team in count_dict: # Counts how many times they won
            count_dict[team] += 1
        
        else:
            count_dict[team] = 1 # Won once

    year = input('Enter a year in the range of 1903 through 2019: ')

    if year == '1904' or year == '1994':
        print("The World Series wasn't played in the year", year)
    elif year < '1903' or year > '2019':
        print('The data for the year', year,'is not included in our database.')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print('The team that won the World Series in ', year, ' is the ', winner, '.', sep='')
        print('They won the World Series', wins, 'times.')

# Call main
main()
