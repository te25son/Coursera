"""
Week 3 - Video 1 - List Mutation
"""

# Lists are MUTABLE, i.e. they can be changed.
# the contents of a list are not fixed and can be changed throughout the program.

lst = list(range(5))
print(lst)

lst[1] = -5  # changes the value at index 1
lst[3] = 23  # changes the value at index 3

print(lst)

# you can add items to a pre-existing list

lst.append(42)  # adds the given number to the END of a list
print(lst)

lst.insert(2, 75)  # inserts the second parameter at the location of the first parameter.
# therefore, this will insert 75 at index 2.
print(lst)

# note that insert does not replace what is at index 2, but moves everything else over.

# you can also another sequence (or list) to the end of a pre-existing list
# using extend. for example...
lst2 = [-67, 50, 102]
lst.extend(lst2)  # like append, extend adds items to the END of your list
print(lst)

# What happens when you try to add a sequence using append?
lst.append(lst2)
print(lst)  # append adds a new list at the last index. so when I print the final index of lst...
print(lst[-1])  # this mess happens. it's not what we want.

# so what about REMOVING items from a list
lst.pop()  # removes the last item of a list
print(lst)
lst.pop(3)  # removes the object at index 3
print(lst)
