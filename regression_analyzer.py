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


"""quadraticRegression(data)
    ----------Get the Quadtratic Regression for the prediction----------"""
def quadraticRegression(data):
    data = list (enumerate (data))
    m11 = sum([x ** 4 for x in data])
    m12 = sum([x ** 3 for x in data])
    m13 = sum([x ** 2 for x in data])
    m14 = sum([y * (x ** 2) for x, y in data])
    
    m21 = sum([x ** 3 for x in data])
    m22 = sum([x ** 2 for x in data])
    m23 = sum([x for x in data])
    m24 = sum([y * x for x, y in data])
    
    m31 = sum([x ** 2 for x in data])
    m32 = sum([x for x in data])
    m33 = len(data)
    m34 = sum([y for y in data])
    
    l = linalg.det([m11, m12, m13],[m21, m22, m23],[m31, m32, m33])
    l1 = linalg.det([m14, m12, m13],[m24, m22, m23],[m34, m32, m33])
    l2 = linalg.det([m11, m14, m13],[m21, m24, m23],[m31, m34, m33])
    l3 = linalg.det([m11, m12, m14],[m21, m22, m24],[m31, m32, m34])
    
    a = l1/l
    b = l2/l
    c = l3/l
    
    return{'a':a, 'b':b, 'c':c}



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

####################### for testing only (Quadratic Regression)#######################

def getQuaddraticYVals():
    data_file = open("GDP.txt", 'r') # r param for 'read' mode
    y_vals = []
    for line in data_file:
        # lines in testdata.txt will have 'new line' characters
        y_vals.append( int( line.replace("\n", "" ) ) )
    return y_vals

y_vals = getQuaddraticYVals()
quadtratic_consts = quadraticRegression(y_vals)
a = quadtratic_consts['a']
b = quadtratic_consts['b']
b = quadtratic_consts['c']

""" Y =   Ax**2       +  Bx     + C"""
model = [(a * (x**2)) + (b * x) + c for x in range(0,14)]

import matplotlib.pyplot as plt

plt.plot(y_vals, 'bo')
plt.plot(model, 'ro')
plt.show()
################################################################
