import matplotlib.pyplot as plt

data_file = open("testdata.txt", 'r') # r param for 'read' mode

data = []

for line in data_file:
    data.append( line.replace("\n", "" ) ) # lines in testdata.txt will have 'new line' characters 

plt.plot(data, 'bo')
plt.show()
