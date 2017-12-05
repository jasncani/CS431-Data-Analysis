from matplotlib import pyplot

def plot(data, model, filename):
    pyplot.plot(data, 'ro')
    pyplot.plot(model, 'b')
    pyplot.savefig(filename)
