"""
Course 3
Week 2 - Video 2 - Tabular Data as Nested Lists
"""


def space():
    print('')


space()

# programming languages by popularity over the years

popularity = [
    ['Language', 2017, 2012, 2007, 2002, 1997, 1992, 1987],
    ['Java', 1, 2, 1, 1, 15, 0, 0],
    ['C', 2, 1, 2, 2, 1, 1, 1],
    ['C++', 3, 3, 3, 3, 2, 2, 5],
    ['C#', 4, 4, 7, 13, 0, 0, 0],
    ['Python', 5, 7, 6, 11, 27, 0, 0],
    ['Visual Basic . NET', 6, 17, 0, 0, 0, 0, 0],
    ['PHP', 7, 6, 4, 5, 0, 0, 0],
    ['Javascript', 8, 9, 8, 7, 23, 0, 0],
    ['Perl', 9, 8, 5, 4, 4, 10, 0]
]

format_string = '{:<18} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4}'

# display languages table
header = popularity[0]
header_row = format_string.format(*header)  # '*' takes a list and turns it into individual arguments
print(header_row)
print('-' * len(header_row))

for language in popularity[1:]:
    print(format_string.format(*language))

space()

# you will probably want to find specific info in a table...
print('Python\'s popularity in 1997:',
      popularity[5][5])  # i had to look this up myself.

space()

# how do we ask the program to do it for us?


def find_col(table, col):
    """
    Returns col index with col header
    """
    return table[0].index(col)


def find_row(table, row):
    """
    Returns row index with row header
    in table, or -1 if row not in table
    """
    for idx in range(len(table)):
        if table[idx][0] == row:
            return idx
    return -1


idx_1997 = find_col(popularity, 1997)
idx_python = find_row(popularity, 'Python')
print('Python\'s popularity in 1997:',
      popularity[idx_1997][idx_python])


