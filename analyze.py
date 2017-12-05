import fileparser
import reganalyzer
import plotter
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
outputFileName = getArgWithExt(outputExtensions)

data = fileparser.parse(inputFileName)

model = reganalyzer.linearRegression(data)

plotter.plot(data, model, outputFileName)
