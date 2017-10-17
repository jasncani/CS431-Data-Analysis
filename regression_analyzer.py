# @param data a 1D array of y values
# @returns [a, b] the constants "a" and "b" for the eqn Y=ax+b
# perform linear regression on "data" using the x values 0...len(data)-1
def linearRegression(data):
	data = list( enumerate( data ) )
	print(data)
	m11 = sum( [x ** 2 for x, y in data] )
	m12 = sum( [x for x, y in data] )
	m13 = sum( [x * y for x, y in data] )
	m21 = sum( [x for x, y in data] )
	m22 = len( data )
	m23 = sum( [y for x, y in data] )
	l = (m11 * m22) - (m12 * m21)
	l1 = (m13 * m22) - (m12 * m23)
	l2 = (m11 * m23) - (m21 * m13)
	a = l1 / l
	b = l2 / l
	return {'a': a, 'b': b}






####################### for testing only #######################

def getYVals():
	data_file = open("GDP.txt", 'r') # r param for 'read' mode
	y_vals = []
	for line in data_file:
		# lines in testdata.txt will have 'new line' characters
		y_vals.append( int( line.replace("\n", "" ) ) )
	return y_vals

y_vals = getYVals()
linear_consts = linearRegression(y_vals)
a = linear_consts['a']
b = linear_consts['b']
model = [a * x + b for x in range(0,14)]

import matplotlib.pyplot as plt

plt.plot(y_vals, 'bo')
plt.plot(model, 'ro')
plt.show()
################################################################
