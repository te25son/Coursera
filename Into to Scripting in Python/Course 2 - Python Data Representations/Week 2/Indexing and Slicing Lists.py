"""
Week 2 - Video 2 - Indexing and Slicing Lists
---------------------------------------------
NOTE:
    Both lists and strings are sequence types, i.e. they each contain a sequence of
    elements. Strings = a sequence of characters. Lists = a sequence of items.
"""

groceries = ['coffee', 'bananas', 'tomatoes', 'pineapple', 'bread']
print(groceries[0])
print(groceries[2])

print('')

# as with strings, use [-1] to reach the last item in a list
print(groceries[-1])

# ...and use negative numbers to index items
print(groceries[-3])
print(groceries[-4])

print('')

# find the length of a list
print(len(groceries))

# but don't go out of range
# print(groceries[len(groceries)])
# print(groceries[22])

print(groceries[len(groceries) - 1])

"""
Indices
-------
list = [10, 7, 6, 5, 2, 78, 3]

item =       10   7   6   5   2  78   3
pos index =   0   1   2   3   4   5   6
neg index =  -7  -6  -5  -4  -3  -2  -1
"""

print('')
print('SLICING')
print('-------')

num_list = list(range(72, 5, -12))
print(num_list)

print(num_list[2:3])
print(num_list[1:4])

print('')

print(num_list[1:])  # everything from index one to the end
print(num_list[:3])  # from index 0 up to but not including index 3

print(num_list[-2:])
print(num_list[1:-4])

print('')

# empty slices
print(num_list[3:2])
print(num_list[10:12])
