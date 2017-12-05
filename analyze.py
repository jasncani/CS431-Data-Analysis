import fileparser
import reganalyzer
from matplotlib import pyplot
import sys

inputExtensions = ['.csv', '.dat', '.txt']
outputExtensions = ['.png', '.jpg']
regressionTypes = ['linear', 'quadratic']

if len(sys.argv) < 4:
    sys.exit("you must supply the input datafile, output filename, and regression type.")

def getArg(extensions):
    for ext in extensions:
        for arg in sys.argv:
            if ext in arg:
                return arg
    return None

inputFileName = getArg(inputExtensions)
if inputFileName == None: sys.exit('no input file detected.')

outputFileName = getArg(outputExtensions)
if outputFileName == None: sys.exit('no output file detected')

regressionType = getArg(regressionTypes)
if regressionType == None: sys.exit('no regression type detected')

data = fileparser.parse(inputFileName)

if regressionType == 'linear':
    model = reganalyzer.linearRegression(data)
elif regressionType == 'quadratic':
    model = reganalyzer.quadraticRegression(data)

pyplot.plot(data, 'ro', label='data')
pyplot.plot(model, 'b', label='regression line')
# pyplot.savefig(filename)
pyplot.legend(loc=4)
pyplot.show()
