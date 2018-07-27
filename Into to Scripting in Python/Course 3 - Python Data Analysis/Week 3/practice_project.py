"""
Course 3
Practice Project!
"""

import csv

DATA_FILE = 'cancer_risk05_v4_county.csv'
DATA_FILE_2 = 'cancer_risk05_v4_county copy.csv'


def read_csv_file(file_name):
    """
        Takes a csv file, parses it, and returns
        a list of lists
    """
    table = []

    with open(file_name, newline='') as csv_file:

        csv_reader = csv.reader(csv_file,
                                skipinitialspace=True,)

        for row in csv_reader:
            table.append(row)

    return table


def print_table(table):
    """
        Prints a nicely formatted table
    """
    for row in table:
        print('{:<4}'.format(row[0]), end='')

        for col in row[1:12]:  # just for testing. don't want to print the entire table.
            if col == row[1]:
                print('{:<33}'.format(row[1]), end='')
            else:
                print('{:>10}'.format(col), end='')

        print('', end='\n')


def write_csv_file(csv_table, file_name, separator, quote_strategy):
    """
        Given a csv table and a new file, read the
        new file into the csv table
    """
    with open(file_name, 'w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file,
                                skipinitialspace=True,
                                delimiter=separator,
                                quoting=quote_strategy)

        for row in csv_table:
            csv_writer.writerow(row)


file_table = read_csv_file(DATA_FILE)
print_table(file_table)

cancer_risk_table = read_csv_file(DATA_FILE)
print(cancer_risk_table[:5])
write_csv_file(cancer_risk_table, DATA_FILE_2, ',', csv.QUOTE_MINIMAL)
cancer_risk_copy = read_csv_file(DATA_FILE_2)
print(cancer_risk_copy[:5])
