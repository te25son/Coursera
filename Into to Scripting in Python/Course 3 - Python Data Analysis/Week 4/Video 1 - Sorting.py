"""
Course 3
Week 4 - Video 1 - Sorting
"""

# learn to use sorting routines that can be found
# in Python's library

import random


def double_space():
    print('', '\n', '')


double_space()
print('normal list:')
data = list(range(1, 11))

print(data)

double_space()
random.shuffle(data)  # randomly shuffles given data
print('shuffled list:')
print(data)

double_space()
data.sort()
print('sorted data:')
print(data)

double_space()
random.shuffle(data)
new_data = sorted(data)  # sorted takes anything you can iterate over
print('reshuffled and resorted data using the sorted() function:')
print(new_data)

# now on to TUPLES!
double_space()
data_tup = tuple(data)
print('a tuple of my data:')
print(data_tup)

double_space()
data_tup_sort = sorted(data_tup)  # returns the tuple as a sorted list
print('sorted tuple (now coverted into a list):')
print(data_tup_sort)

# and what about dictionaries??
double_space()
print('a dictionary:')
my_dict = {key: key ** 2 for key in data_tup}
print(my_dict)

double_space()
my_other_dict = sorted(my_dict)
print('the same dictionary ran with the sorted() function:')
print(my_other_dict)  # returns a sorted list of the keys in a dictionary
print('hmmmmm....')


