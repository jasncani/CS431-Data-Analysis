import csv

def parse(filepath):
    with open(filepath, 'r') as ifile:
        i = csv.reader(ifile, delimiter=',')
        next(i, None)
    
        data = []
        for contents in i:
             data.append(contents[1:])
            
    return data

print(parse('Hotel Occupancy Taxes Collected.csv'))

