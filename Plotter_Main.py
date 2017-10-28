'''
Module: Plotter_Main
Purpose: Used to test the Module "Plotter" and its functions

Created on Oct 28, 2017 (Version 2.0)
@author: Joey S. Amalei

CS431-01
Fall 2017
'''

"""
Import local Plotter Module and NumPy Package to graph values
"""
import csv_parser as parser
import Plotter
import numpy as np

"""
Define test data values
NOTE: number of months is represented by Year 2004-2015
      data.txt and data2.txt are files located together with Main.py current directory
"""
numberOfMonths = 144
rawDataValues = parser.parse("Hotel Occupancy Taxes Collected.csv")
linearRegressionDataValues = np.loadtxt("testdata2.txt")

"""
Set labels for graphical window
"""
Plotter.setGraphLabels("Test Graph", "Number of Months Since (2004 - 2015)", "Hotel Occupancy Taxes Collected ($)")

"""
Graph test data values on console window
"""
Plotter.drawGraph(rawDataValues, linearRegressionDataValues, numberOfMonths)