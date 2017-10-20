##the output is like this...
  [(.....)
   (.....)
   (.....)
   ...]
   
import numpy as np
data = np.recfromcsv('Hotel Occupancy Taxes Collected.csv',delimiter=",",usecols=range(1,13))
print(data)

print("")
print("")
print("")

##output is with years and months
import csv
with open('Hotel Occupancy Taxes Collected.csv', 'r') as ifile:
    read = csv.reader(ifile)
    for data in read:
        print(data)

print("")
print("")
print("")
