import fileparser
import reganalyzer
from matplotlib import pyplot
import sys

inputExtensions = ['.csv', '.dat', '.txt']
outputExtensions = ['.png', '.jpg']

if len(sys.argv) < 2:
    sys.exit("you must supply the input datafile and an output filename.")

def getArgWithExt(extensions):
    for ext in extensions:
        for arg in sys.argv:
            if ext in arg:
                return arg
    return None

inputFileName = getArgWithExt(inputExtensions)
if inputFileName == None: sys.exit('no input file detected.')

outputFileName = getArgWithExt(outputExtensions)
if outputFileName == None: sys.exit('no output file detected')

data = fileparser.parse(inputFileName)

model = reganalyzer.linearRegression(data)

pyplot.plot(data, 'ro', label='data')
pyplot.plot(model, 'b', label='regression line')
# pyplot.plot(projection, 'bo', label='projection')
# pyplot.savefig(filename)
pyplot.legend(loc=4)
pyplot.show()

# plotter.plot(data, model, projection, outputFileName)
