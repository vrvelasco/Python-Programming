# Victor Velasco (TotalRainfall) 9/16/19

# Variables
totalRainfall = 0.0
monthRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0

years = int(input('Enter the number of years: '))

for year in range(years):
    print('For year', year + 1, ':')
    for month in range(12):
        monthRainfall = float(input('Enter the rainfall for the month: '))
        totalMonths += 1
        totalRainfall += monthRainfall
        
averageRainfall = totalRainfall / totalMonths

print('For ', totalMonths, 'months')
print('Total Rainfall: ', format(totalRainfall, ',.2f'), 'inches.')
print('Average Rainfall: ', format(averageRainfall, ',.2f'), 'inches.')
