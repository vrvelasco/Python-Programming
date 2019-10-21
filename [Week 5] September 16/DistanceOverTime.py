# Victor Velasco (DistanceOverTime) 9/16/19

distance = 0.0
speed = 0.0
time = 0

speed = float(input('Speed of vehicle in miles per hour: '))
time = int(float(input('Enter the number of hours traveled: ')))

print('Hour\tDistance traveled')
print('-------------------------')

for hour in range(1, time + 1):
    distance = hour * speed
    print(hour, '\t', distance)


