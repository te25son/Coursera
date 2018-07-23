"""
Course 3
Week 3 - Video 4 - CSV Dictionary Reader
"""

import csv


MONTHS = (
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
)


def dictparse(csvfilename, keyfield):
    """
    Reads a CSV file and returns the data as a dictionary
    within a dictionary
    """
    table = {}
    with open(csvfilename, 'rt', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True)
        for row in csvreader:
            table[row[keyfield]] = row

    return table


file = 'hightemp.csv'
print(dictparse(file, 'City'))
print('')


def print_table(table):
    """
    Prints out a table, which must be a dictionary of
    dictionaries, in nice, organized way
    """
    print("City               ", end='')
    for month in MONTHS:
        print('{:>6}'.format(month), end='')
    print('')
    for name, row in table.items():
        print('{:<19}'.format(name), end='')
        for month in MONTHS:
            print('{:>6}'.format(row[month]), end='')
        print('', end='\n')


table = dictparse(file, 'City')
print_table(table)