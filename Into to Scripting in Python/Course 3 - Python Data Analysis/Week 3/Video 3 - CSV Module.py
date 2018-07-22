"""
Course 3
Week 3 - Video 3 - Python's CSV Module
"""

import csv

file = 'hightemp2.csv'

def parse(csvfilename):
    """
    Takes a CSV file and parses it to return
    a list of lists
    """
    table = []
    with open(csvfilename, 'r') as csvfile:
        csvreader = csv.reader(csvfile,
                               skipinitialspace=True)  # if there are spaces at the begininning
        # of a field, throw them away
        for row in csvreader:
            table.append(row)

    return table


def print_table(table):
    """
    Returns a nicely formatted table :)
    """
    for row in table:
        print('{:<19}'.format(row[0]), end='')

        for col in row[1:]:
            print('{:>4}'.format(col), end='')

        print('', end='\n')


table = parse(file)
print_table(table)
