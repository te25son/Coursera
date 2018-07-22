"""
Course 3
Week 3 - Video 2 - Parsing CSV Files
"""

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        print("{:<19}".format(row[0]), end='')
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

table = parse("hightemp.csv")
print_table(table)

print("")
print("")

table2 = parse("hightemp2.csv")
print_table(table2)
