"""
UPDATE: Friday - 10/27/2017
-Added additonal algorithm step to parse STRING lists created from the
csv.reader() function to INT type which will be the RETURN value
"""

"""
Import Python package csv to use for reading files
"""
import csv

"""
Define function parse() to read CSV files to be parsed
"""
def parse(filePath):

    """
    Define an empty list to hold our INT type values to represent tax collected data values
    """
    data = []

    """
    Open and read CSV file
    """
    with open(filePath, 'r') as iFile:
        i = csv.reader(iFile, delimiter=',')
        next(i, None)

        """
        Algorithm #1 - Outer Loop
        =========================
        Read next row in CSV file onto variable 'rowListOfValues' that will hold a list of strings containing
        csv data values
        """
        for rowListOfValues in i:

             """
             Algorithm #2 - Inner Loop
             =========================
             Read next column in CSV file onto variable 'columnListOfValues' that will hold
             a SINGLE STRING value representing the tax collected data value.

             NOTE: using '[1:]' in list is to ommit CSV file's 1st row and 1st column headings
             """
             for columnSingleDataValue in rowListOfValues[1:]:
                 # Parse string value from CSV file to INT type value to represent the tax collected data values
                 taxCount = int(columnSingleDataValue)
                 # Add taxCount value onto 'data' list
                 data.append(taxCount)

    """
    Return list of all tax collected data values from CSV file that has
    been parsed from STRING data type to INT data type
    """
    return data
