# Victor Velasco (Trig Plot) 10/14/19

import pylab

x_values = pylab.linspace(0, 4 * pylab.pi, 100)
y1_values = pylab.sin(x_values)
y2_values = pylab.cos(x_values)

pylab.title('Sine and Cosine Plot')
pylab.plot(x_values, y1_values, 'b')
pylab.plot(x_values, y2_values, 'r')
pylab.show()
