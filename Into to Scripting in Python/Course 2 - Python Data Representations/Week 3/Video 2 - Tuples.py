"""
Week 3 - Video 2 - Tuples
"""

# A tuple, like a list, is a sequence type.
# Unlike a list, a tuple is IMMUTABLE, meaning it cannot be changed.

my_list = [5, 8, 7, 9, 10]
my_tuple = (5, 8, 7, 9, 10)  # a tuple uses parenthesis instead of square brackets

print(my_list, my_tuple)
print(my_tuple[1])
print(my_list[1])
print(my_tuple[-1])
print(my_list[-1])

# OMG it's the SAME!!!

print(my_tuple[: 2])
print(my_tuple[2 :])
print(my_list[: 2])
print(my_list[2 :])

# But not really...

my_list[1] = 8
print(my_list)
# my_tuple[1] = 8 == TypeError: 'tuple' object does not support item assignment
# This is a big no-no with tuples. No changing. Why? They're immutable.

# METHODS USED WITH TUPLES
print(my_tuple.index(7))  # prints the location of 7 (if it exists) in your tuple
print(my_tuple.count(3))  # counts the num of times 3 occurs in your tuple

# we can also use the tuple function to make tuples out of another sequence of elements.
another_list = [67, 12, 15, 102]
another_tuple = tuple(another_list)
print(another_list)
print(another_tuple)

print(tuple(range(0, 5)))
print(tuple(range(0, 101, 10)))
