"""
Course 4
Week 3 - Video 1 - Python Sets
"""

# Learn about Python Sets
#
# similar to lists and tuples
# however, they do not come in a specific order
# nor do they contain duplicates


# make a set using curly braces
set_nums = {3, 4, 1, 6, 5, 7, 2}  # notice the output is in a diff order
print(set_nums)

set_lets = {'a', 'b', 'c', 'a', 'b', 'c'}  # output gets rid of duplicates
print(set_lets)

# find the length of set_lets
print(len(set_lets))  # output will be 3

# iterate over set lets
for letter in set_lets:
    print(letter)  # this will not be in a specific order
print('')

# iterate over ordered set lets
for letter in sorted(set_lets):
    print(letter)  # now the output is in order

# print an empty set
set_empty = {}
print(set_empty, type(set_empty))  # output will be <class 'dict'> NOT <class 'set'>

# fix that...
dict_empty = set_empty
set_empty = set()
print(set_empty, type(set_empty))  # set function without arguments creates an empty set
print('')

# use set() to turn other sequence types into sets
a_list = [1, 3, 3, 6, 2, 7, 1, 9]
a_set = set(a_list)
print(a_set)

# quickly create a set of a range of numbers
range_set = set(range(1, 11))
print(range_set)
print('')

# add an element to a set
range_set.add(11)
print(range_set)  # number 11 added to range_set

# remove element from set
# NOTE : sets are not ordered, so the element removed will be arbitrary
num = range_set.pop()
print(num)
print(range_set)

# add the number back onto the set
range_set.add(num)

# use .discard() to remove a particular element from the set
range_set.discard(6)
print(range_set)  # the number six has been removed from the set
print('')

# add a set to another set
set_nums.update(set_lets)
print(set_nums)
