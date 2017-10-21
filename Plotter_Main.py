'''
Module: Plotter_Main
Purpose: Used to test the Module "Plotter" and its functions

Created on Oct 21, 2017
@author: Joey S. Amalei

CS431-01
Fall 2017
'''

"""
Import local Plotter Module and NumPy Package to graph values
"""
import Plotter
import numpy as np

"""
Define test data values
NOTE: number of months is represented by Year 2004-2015
      testdata.txt and testdata2.txt are files located together with Plotter_Main.py current directory
"""
numberOfMonths = 144
rawDataValues = np.loadtxt("testdata.txt")
linearRegressionDataValues = np.loadtxt("testdata2.txt")

"""
Set labels for graphical window
"""
Plotter.setGraphLabels("Test Graph", "Number of Months", "Hotel Occupancy Taxes Collected")

"""
Graph test data values on console window
"""
Plotter.drawGraph(rawDataValues, linearRegressionDataValues, numberOfMonths)
