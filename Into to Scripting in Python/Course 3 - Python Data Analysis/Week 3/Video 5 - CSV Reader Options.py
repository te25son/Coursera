"""
Course 3
Week 3 - Video 5 - CSV Reader Options
"""

import csv


def double_space():
    print('', '\n', '')


double_space()


def dictparse(csvfilename, keyfield, separator, quote, quotestrategy):
    """
    Parses a CSV file and returns a dictionary of
    dictionaries.
    """
    table = {}

    with open(csvfilename, 'rt', newline='') as csvfile:
        csvreader = csv.DictReader(
            csvfile,
            skipinitialspace=True,
            delimiter=separator,  # what char should separate the data in the file
            quotechar=quote,  # specifies what the quote character is in file
            quoting=quotestrategy
        )

        for row in csvreader:
            table[row[keyfield]] = row

    return table, csvreader.fieldnames
    # fieldnames returns a list of the field names in a file, so
    # we don't have to know them beforehand :)


def print_table(table, fieldnames):
    """
    Prints out a nicely formatted table!
    """
    print('{:<19}'.format(fieldnames[0]), end='')
    for field in fieldnames[1:]:
        print('{:>6}'.format(field), end='')

    print('')

    for name, row in table.items():
        print('{:<19}'.format(name), end='')
        for field in fieldnames[1:]:
            print('{:>6}'.format(row[field]), end='')
        print('', end='\n')


file = 'hightemp.csv'
file2 = 'hightemp2.csv'
table1, fieldnames1 = dictparse(
    file,
    'City',
    ',',
    '"',
    csv.QUOTE_MINIMAL
)
# with QUOTE_MINIMAL quotes are only being used when necessary
# the reader assumes all values are going to be strings

print(fieldnames1)
double_space()
print_table(table1, fieldnames1)
double_space()

table2, fieldnames2 = dictparse(
    file2,
    'City',
    ',',
    '"',
    csv.QUOTE_NONNUMERIC
)
# with QUOTE_NONNUMERIC, the reader dictates that every column that is not numerical
# must be quoted and thus a string. Something that is NOT quoted must be a number and so
# returns floating point numbers for the values not quoted.

print_table(table2, fieldnames2)
