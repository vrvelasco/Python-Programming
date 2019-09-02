# Victor Velasco 9/1/19

import math
pie = math.pi

# Get input
print('This program takes the radius of two different circles, calculates the area of both circles, and then compares the area\n')
radiusA = float(input('Please enter the radius of the first circle: '))
radiusB = float(input('Please enter the radius of the second circle: '))

# Math
areaA = radiusA * radiusA * pie
areaB = radiusB * radiusB * pie

# Display
print('The area of circle 1 is:', format(areaA, ',.2f'), ' and the area of circle 2 is:', format(areaB, ',.2f'))

# Compare
if areaA > areaB:
  print('\n\nCircle 1 is bigger')
elif areaB > areaA:
  print('\n\nCircle 2 is bigger')
else:
  print('\n\nThe area is the same.')

