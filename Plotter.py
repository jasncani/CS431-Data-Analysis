'''
Module: plotter
Purpose: This module is to plot and display values onto a graphical console window

Last Edit By: Joey S. Amalei (Sat. 12/2/2017)

CS431-01
Fall 2017
'''

"""
Import PyPlot Package from Python to graph
"""
import matplotlib.pyplot as plt

"""
Global Variables
"""
GRAPH_TITLE = ''
GRAPH_X_LABEL = ''
GRAPH_Y_LABEL = ''
# 'r' - Red, 'b' - Blue, 'm' - Magenta, 'c' - Cyan, 'g' - Green
COLOR_LIST = ['r', 'b', 'm', 'c', 'g']
NEXT_COLOR_POINTER = 0

"""
Define Functions to use for Plotter Module
"""

#Assign graph format values
#@param graphTitle - The graph's title name
#@param xLabel - The graph's x-axis label name
#@param yLabel - The graph's y-axis label name
#@return - none
def setGraphLabels(graphTitle, xLabel, yLabel):
    """
    Update Global Variables
    """
    global GRAPH_TITLE, GRAPH_X_LABEL, GRAPH_Y_LABEL
    GRAPH_TITLE = graphTitle
    GRAPH_X_LABEL = xLabel
    GRAPH_Y_LABEL = yLabel

#Plot the data values onto the figure windows
#@param dataValues - list of 1D array containing y values
#@param typeOfGraph - what graph to draw on graphical window
#   optional - 'scatter'
#@return - none
def drawGraph(dataValues, typeOfGraph):  
    """
    Fill values to the x list to be used as our X-Axis tick mark labels
    """
    x = []
    for i in range (len(dataValues)):
        x.append(i)
        
    """
    Plot x and y values onto graph
    """
    # Graph function for rawData values
    # Argument c - changes the color of the scatter dot graph
    if (typeOfGraph == 'scatter'):
        global COLOR_LIST, NEXT_COLOR_POINTER 
        plt.scatter(x, dataValues, c=COLOR_LIST[NEXT_COLOR_POINTER])
        NEXT_COLOR_POINTER += 1
    else:
        # Graph function for linearRegressionData values
        # Argument c - changes the color of the line graph
        plt.plot(x, dataValues, c=COLOR_LIST[NEXT_COLOR_POINTER])
        NEXT_COLOR_POINTER += 1

#Display graphical window containing drawn plot values
#param fileName - The string name of the PNG file to create of graph figure
#@return - none
def displayGraph(fileName):
    """
    Assign lables on the graphical window
    figsize is shown using inches for graphical window size
    """
    global GRAPH_TITLE, GRAPH_X_LABEL, GRAPH_Y_LABEL
    plt.title(GRAPH_TITLE)
    plt.xlabel(GRAPH_X_LABEL)
    plt.ylabel(GRAPH_Y_LABEL)

    plt.tight_layout()
    plt.savefig(fileName)
    plt.show()
