"""
Module: main_module
Purpose: Compute regressions of data values given, plot the data values,
         and then display a graph of their plot values

Last Edited By: Joey S. Amalei (Sat. 12/2/2017)

CS431-01
Fall 2017
"""

"""
Import required modules
"""
import csv_parser as parser
import plotter
import regression_analyzer as reg
import sys
import os
import time


"""
QUICK RUN - SINGLE GRAPH ONLY TO DISPLAY
Handle Command Line Argument Index locations
[1] - Input data file path
[2] - What regression graph to display
[3] - Output figure image file name
"""
# Any commmand line arguments passed?
if (len(sys.argv) > 1):
    # Clear console screen - 'cls' for Windows / 'clear' Linux & Mac OSX
    os.system('cls')

    # Welcome Title Program Screen Text
    print("====================================")
    print(" GROUP 2 - REGRESSION SOFTWARE")
    print(" CS431-01")
    print(" Fall 2017")
    print("====================================")
    print()
    
    """
    LOOP 1 - Process available command line arguments
    """
    inputFilePath = sys.argv[1]

    """
    Plot and draw the raw input data values onto figure window
    """
    rawDataValues = parser.parse(inputFilePath)
    plotter.drawGraph(rawDataValues, 'scatter')
    
    # What regression graph to display?
    if (sys.argv[2] == 'linear'):
        linearRegressionDataValues = reg.linearRegression(parser.parse(inputFilePath))
        plotter.drawGraph(linearRegressionDataValues, 'line')
    elif (sys.argv[2] == 'exponential'):
        exponentialRegressionDataValues = reg.exponentialRegression(parser.parse(inputFilePath))
        plotter.drawGraph(exponentialRegressionDataValues, 'line')
    else:
        quadraticRegressionDataValues = reg.quadraticRegression(parser.parse(inputFilePath))
        plotter.drawGraph(quadraticRegressionDataValues, 'line')

    # Display drawn plotted graph onto window
    plotter.displayGraph(sys.argv[3])
else:
    """
    LOOP 2 - Enter an infinite loop for user input interaction on console window
    """
    # Clear console screen - 'cls' for Windows / 'clear' Linux & Mac OSX
    os.system('cls')

    # Welcome Title Program Screen Text
    print("====================================")
    print(" GROUP 2 - REGRESSION SOFTWARE")
    print(" CS431-01")
    print(" Fall 2017")
    print("====================================")
    print()
    print()

    """
    USER INPUT #1
    """
    inputFilePath = input("Enter data file path (include .csv - file extension): ")
    graphTitle = input("Enter the title name of the graph: ")
    xLabel = input("Enter the name of the x-axis for the graph: ")
    yLabel = input("Enter the name of the y-axis for the graph: ")

    """
    Plot and draw the raw input data values onto figure window
    """
    rawDataValues = parser.parse(inputFilePath)
    plotter.drawGraph(rawDataValues, 'scatter')
    
    # Request user what regression to plot and draw on figure
    done = False
    
    while (done != True):
        # Clear console screen - 'cls' for Windows / 'clear' Linux & Mac OSX
        os.system('cls')
        """
        USER INPUT #2
        """
        # What does the user want to do?
        print("===================================================")
        print(" SELECT REGRESSION GRAPH OPTIONS TO DRAW ON FIGURE")
        print()
        print(" 1 - Linear Regression")
        print(" 2 - Exponential Regression")
        print(" 3 - Quadratic Regression")
        print()
        print(" 4 - Exit sub-menu and display figure on screen")
        print("===================================================")
        print()

        # Process user selection of options
        menuOptionValue = input("Enter a number as your option of choice: ")
        if (menuOptionValue == '1'):
            linearRegressionDataValues = reg.linearRegression(parser.parse(inputFilePath))
            plotter.drawGraph(linearRegressionDataValues, 'line')
            print()
            print("===================================================")
            print(" DRAWING GRAPH ON FIGURE WINDOW NOW...")
            print(" Returning back to sub-menu")
            print("   for more options to select...")
            print("===================================================")
            time.sleep(3)
        elif (menuOptionValue == '2'):
            exponentialRegressionDataValues = reg.exponentialRegression(parser.parse(inputFilePath))
            plotter.drawGraph(exponentialRegressionDataValues, 'line')
            print("===================================================")
            print(" DRAWING GRAPH ON FIGURE WINDOW NOW...")
            print(" Returning back to sub-menu")
            print("   for more options to select...")
            print("===================================================")
            time.sleep(3)
        elif (menuOptionValue == '3'):
            quadraticRegressionDataValues = reg.quadraticRegression(parser.parse(inputFilePath))
            plotter.drawGraph(quadraticRegressionDataValues, 'line')
            print("===================================================")
            print(" DRAWING GRAPH ON FIGURE WINDOW NOW...")
            print(" Returning back to sub-menu")
            print("   for more options to select...")
            print("===================================================")
            time.sleep(3)
        elif (menuOptionValue == '4'):
            print("===================================================")
            print(" EXITING SUB-MENU NOW...")
            print()
            print(" Will now prepare figure window to be displayed...")
            print("===================================================")
            time.sleep(3)
            done = True
        else:
            print("That option is not acceptable. Please try again.")
            time.sleep(5)

    """
    USER INPUT #3
    """
    # Clear console screen - 'cls' for Windows / 'clear' Linux & Mac OSX
    os.system('cls')

    # Display Heading Text
    print("====================================")
    print(" CREATION OF FIGURE IMAGE FILE")
    print(" IN .PNG FILE EXTENSION")
    print("====================================")
    print()
    # Request user for output file name
    outputFileName = input("Enter figure image file name (include .png - file extension): ")
    
    # Display user's plotted graph on window
    plotter.setGraphLabels(graphTitle, xLabel, yLabel)
    plotter.displayGraph(outputFileName)

"""
Display Exit Message
"""
# Clear console screen - 'cls' for Windows / 'clear' Linux & Mac OSX
os.system('cls')
print("===================================================")
print(" THANK YOU FOR USING THE REGRESSION SOFTWARE!")
print()
print(" CREDITS TO:")
print(" Gabrielson Aguilar")
print(" Claudette Aguon")
print(" Joey Amalei")
print(" Jason Bacani")
print(" Jose-Peter Charfauros")
print()
print(" CS431-01 | Fall 2017")
print("===================================================")
