# Victor Velasco (Rectangle) 9/9/19

length_a = float(input('Enter the length for Rectangle A: '))
width_a = float(input('Enter the width for Rectangle A: '))

length_b = float(input('Enter the length for Rectangle B: '))
width_b = float(input('Enter the width for Rectangle B: '))

# Math
area_a = length_a * width_a
area_b = length_b * width_b

# Display
print('Area for Rectangle A:', format(area_a, ',.2f'))
print('Area for Rectangle B:', format(area_b, ',.2f'))

# Compare
if area_a > area_b:
    print('Area for Rectangle A is greater than Rectangle B.')
elif area_a < area_b:
    print('Area for Rectangle B is greater than Rectangle A.')
else:
    print('Area for Rectangle A and Rectangle B are equal.')
