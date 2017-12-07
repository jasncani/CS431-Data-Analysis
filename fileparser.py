# fileparser module for module for Dr. Zou's Fall 2017 CS431-01 class
# Purpose: provide functions extracting data from data files

# Parses a data file and returns the data in a list, skipping the
# header row and id column.
# @param filename the name of the file to be parsed
# @returns a list containing the the data in a data file
def parse(filename):
    openFile = open(filename, 'r') # open file as read-only
    data = []
    next(openFile) # skip first line in file
    for line in openFile:
        line = line.replace('\n', '')
        row = line.split(',')
        for col in row[1:]: # skip first column in row
            data.append(float(col))
    return data
