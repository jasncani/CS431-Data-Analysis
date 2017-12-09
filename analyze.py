# Main Module for Dr. Zou's Fall 2017 CS431-01 class
# Purpose: interface between the user and the other modules needed to
# compute a statistical model of a given dataset

import fileparser
import reganalyzer
from matplotlib import pyplot
import sys

if len(sys.argv) < 5:
    sys.exit("you must supply the input datafile, regression type, projection amount, and output filename")

inputFileName = sys.argv[1]
regressionType = sys.argv[2]
projAmt = int(sys.argv[3])
outputFileName = sys.argv[4]

data = fileparser.parse(inputFileName)

if regressionType == 'linear':
    model = reganalyzer.linearProjection(data, projAmt)
elif regressionType == 'quadratic':
    model = reganalyzer.quadraticProjection(data, projAmt)
elif regressionType == 'exponential':
    model = reganalyzer.exponentialProjection(data, projAmt)
else:
    sys.exit("unkown regression type provided")

outputFile = open(outputFileName + '.dat', 'w')
outputFile.write('data,%s\n' % ','.join([str(x) for x in data]))
outputFile.write('model,%s\n' % ','.join([str(x) for x in model]))
outputFile.close()

pyplot.plot(data, 'ro', label='data')
pyplot.plot(model, 'b', label='regression line')
pyplot.savefig(outputFileName + '.png')
pyplot.legend(loc=4)
pyplot.title(outputFileName)
pyplot.show()
