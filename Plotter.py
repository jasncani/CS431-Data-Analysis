'''
Module: Plotter
Purpose: This module is to plot and display values onto a graphical console window

Created on Oct 21, 2017
@author: Joey S. Amalei

CS431-01
Fall 2017
'''

"""
Import PyPlot Package from Python to graph
"""
import matplotlib.pyplot as plt


"""
Define Functions to use for Plotter Module
"""
def setGraphLabels(graphTitle, xLabel, yLabel):
    """
    Assign lables on the graphical window
    """
    plt.title(graphTitle)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

def drawGraph(rawData, linearRegressionData, numOfMonths):  
    """
    Fill values to the x list to be used as our X-Axis tick mark labels
    """
    x = []
    for i in range (numOfMonths):
        x.append(i)
        
    """
    Plot x and y values onto graph
    """
    # Graph function for rawData values
    # Argument c - changes the color of the scatter dot graph
    plt.scatter(x, rawData, c="r")
    # Graph function for linearRegressionData values
    # Argument c - changes the color of the line graph
    plt.plot(x, linearRegressionData, c="b")
    
    """
    Graph and display graphical values onto console window
    """
    plt.show()