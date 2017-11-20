import csv_parser
import regression_analyzer
import plotter
import sys
import math

input_file_path = sys.argv[1]
data = csv_parser.parse(input_file_path)

quadratic_constants = regression_analyzer.quadraticRegression(data)
print (quadratic_constants)
x_values = len(data)
model = [quadratic_constants['a'] * x ** 2 + quadratic_constants['b'] * x + quadratic_constants['c'] for x in list(range(0, x_values))]

plotter.drawGraph(data, model, x_values)

exp_consts = regression_analyzer.exponentialRegression(data)
print (exp_consts)
model = [exp_consts['a'] * math.exp(exp_consts['b'] * x) for x in list(range(0, x_values))]
plotter.drawGraph(data, model, x_values)
