import csv

def parse(filepath):
    with open(filepath, 'r') as ifile:
        contents = csv.reader(ifile, delimiter=',')
        next(contents, None)
    
        data1 = []
        for data in contents:
             data1.append(data[1:])
            
    return data1

print(parse('Hotel Occupancy Taxes Collected.csv'))
