# Victor Velasco 9/1/19

import math
pie = math.pi

# Get input
print('This program takes the radius of two different circles, calculates the area of both circles, and then compares the area\n')
radiusA = float(input('Please enter the radius of the first circle: ')
radiusB = float(input('Please enter the radius of the second circle: ')

# Math
areaA = radiusA * radiusA * pie
areaB = radiusB * radiusB * pie

# Compare
if areaA > areaB:
  print(
