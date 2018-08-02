"""
Course 3
Week 4 - Video 3 - Advanced Sorting
"""

import random

# create a shuffled list of numbers
print('')
data = list(range(1, 11))
random.shuffle(data)
print('shuffled data:', data)
print('')

# use sort to sort the shuffled numbers
data.sort()
print('ascending sort:', data)
data.sort(reverse=True)
print('')
print('descending sort:', data)
print('')

# create a list of tuples
data_tups = [(item, random.randrange(3, 15)) for item in data]
print('data tuples:', data_tups)
print('')

# sort the list of tuples
data_tups.sort()  # sorts by the first element of the tuple
print('sorted list of tuples:', data_tups)
data_tups.sort(key=lambda pair: pair[1])
print('')
print('sorted list of tuples by the tuples second element:', data_tups)
data_tups.sort(key=lambda pair: pair[0] * pair[1], reverse=True)
print('')
print('''sorted the data by the product of both elements in the tuple
in descending order:''', data_tups)
print('')

# shuffle the list of tuples
random.shuffle(data_tups)
print('shuffled list of tuples:', data_tups)
print('')

# use SORTED() to sort the list of tuples
new_data_tups = sorted(data_tups, key=lambda pair: pair[1], reverse=True)
print('sorted list of tuples:', new_data_tups)
