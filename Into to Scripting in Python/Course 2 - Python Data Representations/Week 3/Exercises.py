"""
Week 3 - Exercises
"""

import random

# 1
example_list = [10, 20, 30, 40]
example_list[2] = 0

print(example_list)

# 2
example_list = [1, 3, 4, 7, 11, 15]
example_list[1:3] = [0, 0, 0]

print(example_list)

# 3
example_list = [4, 6, 2, 1, 9, 10]
example_list.append(0)

print(example_list)

# 4
example_list = [0, 5, 3, 77, 21]
example_list += [0, 0, 0]  # this implements the __iadd__ method for iterating over lists
# it does the same thing the extend method does

print(example_list)

# or you can als try it a different way...
example_list = [0, 5, 3, 77, 21]
example_list.extend([0, 0, 0])

print(example_list)

# 5
example_list = [1, 2, 3, 4]
new_list = example_list + [0, 0, 0]

print(new_list)

# 6
example_list = [0, 1, 2, 3, 4]

for num in [0, 0, 0]:
    example_list.append(num)

print(example_list)

# 7
example_list = [2, 4, 6, 8]
example_tuple = tuple(example_list)

print(example_list)
print(example_tuple)

# 8
example_list = [2, 3, 4, 5, 6]
random.shuffle(example_list)

print(example_list)

# 9
def flatten(nested_list):
    """
    Given a list with lists as items,
    return a list joining all sub lists.
    """
    new_list = []
    for item in nested_list:
        new_list.extend(item)
    return new_list

print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))

# 10
def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order.
    """
    cleanlist = []
    for x in items:
        if x not in cleanlist:
            cleanlist.append(x)
    return cleanlist

print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))
