# Regression Analyzer module for Dr. Zou's Fall 2017 CS431-01 class
# Purpose: provide functions for computing least squares linear, exponential,
# and quadratic regression

import math
import numpy as np

# perform linear least squares regression on a data set
# @param data a 1D array of numerical data
# @returns a least squares model of the data conforming to the eqn y=ax+B
def linearRegression(data):
    data = list(enumerate(data))
    m11 = sum([x ** 2 for x, y in data])
    m12 = sum([x for x, y in data])
    m13 = sum([x * y for x, y in data])
    m21 = sum([x for x, y in data])
    m22 = len(data)
    m23 = sum([y for x, y in data])
    l = (m11 * m22) - (m12 * m21)
    l1 = (m13 * m22) - (m12 * m23)
    l2 = (m11 * m23) - (m21 * m13)
    a = l1 / l
    b = l2 / l
    model = [(a * (x)) + b for x in range(0, len(data))]
    return (model)

# perform exponential least square regression on a data set
# @param data a 1D array of numerical data
# @returns a least squares model of the data conforming to the eqn y=ae^(b * x)
def exponentialRegression(data):
    linearlyTransformedData = [math.log(y) for y in data]
    linearModel = linearRegression(linearlyTransformedData)
    model = [math.exp(y) for y in linearModel]
    return(model)

# perform quadratic least squares regression on a data set
# @param data a 1D array of numerical data
# @returns a least squares model of the data conforming to the eqn y=ax^2+bx+c
def quadraticRegression(data):
    data = list(enumerate(data))
    m11 = sum([x ** 4 for x, y in data])
    m12 = sum([x ** 3 for x, y in data])
    m13 = sum([x ** 2 for x, y in data])
    m14 = sum([y * (x ** 2) for x, y in data])
    m21 = sum([x ** 3 for x, y in data])
    m22 = sum([x ** 2 for x, y in data])
    m23 = sum([x for x, y in data])
    m24 = sum([y * x for x, y in data])
    m31 = sum([x ** 2 for x, y in data])
    m32 = sum([x for x, y in data])
    m33 = len(data)
    m34 = sum([y for x, y in data])
    a1 = np.array([[m11, m12, m13],[m21, m22, m23],[m31, m32, m33]])
    a2 = np.array([[m14, m12, m13],[m24, m22, m23],[m34, m32, m33]])
    a3 = np.array([[m11, m14, m13],[m21, m24, m23],[m31, m34, m33]])
    a4 = np.array([[m11, m12, m14],[m21, m22, m24],[m31, m32, m34]])
    l = np.linalg.det(a1)
    l1 = np.linalg.det(a2)
    l2 = np.linalg.det(a3)
    l3 = np.linalg.det(a4)
    a = l1/l
    b = l2/l
    c = l3/l
    model = [(a * (x * x)) + (b * x) + c for x in range(0, len(data))]
    return(model)
