"""
Module: regression_analyzer
Purpose: Compute linear, exponential, and quadratic regressions of data values

Last Edited By: Joey S. Amalei (Sat. 12/2/2017)

CS431-01
Fall 2017
"""

"""
Import packages to compute matrices for linear regression
"""
import math
import numpy as np


# @param data a 1D array of y values
# @returns 1D array of computed y values
# perform linear regression on "dataValues"
def linearRegression(dataValues):
        data = list(enumerate(dataValues))

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
        
        """
        Formula:
        Y = Ax + B
        """
        model = [(a * (x)) + b for x in range(0, len(dataValues))]
        return (model)

# @param data a 1D array of y values
# @returns 1D array of computed y values
# perform exponential regression on "dataValues"
def exponentialRegression(dataValues):
        """
        Linearly transform data values before processing exponential regression
        """
        linearlyTransformedData = [math.log(y) for y in dataValues]

        # Perform linear regression algorithm on linearly transformed data values
        data = list(enumerate(linearlyTransformedData))

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

        """
        Formula:
        Y = Ae^(B * x)
        """
        A = math.exp(b)
        B = a
        
        model = [A * math.exp(B * x) for x in range(0, len(dataValues))]
        return (model)

# @param dataValues a 1D array of y values
# @returns 1D array of computed y values
# perform quadratic regression on "dataValues"
def quadraticRegression(dataValues):
        data = list(enumerate(dataValues))

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

        # Create an array to find its determinant value
        a1 = np.array([[m11, m12, m13],[m21, m22, m23],[m31, m32, m33]])
        a2 = np.array([[m14, m12, m13],[m24, m22, m23],[m34, m32, m33]])
        a3 = np.array([[m11, m14, m13],[m21, m24, m23],[m31, m34, m33]])
        a4 = np.array([[m11, m12, m14],[m21, m22, m24],[m31, m32, m34]])

        # Find determinant for each array
        l = np.linalg.det(a1)
        l1 = np.linalg.det(a2)
        l2 = np.linalg.det(a3)
        l3 = np.linalg.det(a4)

        a = l1/l
        b = l2/l
        c = l3/l

        """
        Formula:
        Y = Ax^2 + Bx + C
        """
        model = [(a * (x**2)) + (b * x) + c for x in range(0, len(dataValues))]
        return (model)
