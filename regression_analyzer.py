import math
import numpy.linalg as linalg

# @param data a 1D array of y values
# @returns [a, b] the constants "a" and "b" for the eqn Y=ax+b
# perform linear regression on "data" using the x values 0...len(data)-1
def linearRegression(data):
	data = list( enumerate( data ) )
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

def exponentialRegression(data):
    linearlyTransformedData = [math.log(y) for y in data]
    linearConstants = linearRegression(linearlyTransformedData)
    A = math.exp(linearConstants['b'])
    B = linearConstants['a']
    return {'a': A, 'b': B}


"""quadraticRegression(data)
    ----------Get the Quadtratic Regression for the prediction----------"""
def quadraticRegression(data):
    data = list (enumerate (data))
    m11 = sum([x ** 4 for x,y in data])
    m12 = sum([x ** 3 for x,y in data])
    m13 = sum([x ** 2 for x,y in data])
    m14 = sum([y * (x ** 2) for x,y in data])

    m21 = sum([x ** 3 for x,y in data])
    m22 = sum([x ** 2 for x,y in data])
    m23 = sum([x for x,y in data])
    m24 = sum([y * x for x,y in data])

    m31 = sum([x ** 2 for x,y in data])
    m32 = sum([x for x,y in data])
    m33 = len(data)
    m34 = sum([y for x,y in data])

    l = linalg.det([[m11, m12, m13],[m21, m22, m23],[m31, m32, m33]])
    l1 = linalg.det([[m14, m12, m13],[m24, m22, m23],[m34, m32, m33]])
    l2 = linalg.det([[m11, m14, m13],[m21, m24, m23],[m31, m34, m33]])
    l3 = linalg.det([[m11, m12, m14],[m21, m22, m24],[m31, m32, m34]])

    a = l1/l
    b = l2/l
    c = l3/l

    return{'a':a, 'b':b, 'c':c}
