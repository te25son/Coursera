"""
Week 1 - Video 2 - Indexing Strings
"""

# INDEXING and SUBSCRIPTING are terms used to describe what we do when
# we access specific characters within a string

phrase = 'Python is pretty cool!'
print(phrase[0])
fourth = phrase[3]
print(fourth)

# type is a built in function that takes a parameter and returns a string
# describing what class (e.g. string, float, integer, etc.) the given parameter is in.
print(type(phrase))
print(type(fourth))
print(type(True))
print(type(9.6787))
print(type(0))

# you can also find the length of a string using the built-in
# function "len"
print(len(phrase))
phraselen = len(phrase)

# getting the last character in a string
print(phrase[phraselen - 1])  # remember: phraselen is actually an integer,
# so an integer - an integer = an integer :)
print(phrase[-1])  # -1 will always represent the LAST index in a string

# print the fourth from last character in a string
print(phrase[-19])

# THERFORE there are TWO ways to index a string
# with either POSITIVE or NEGATIVE numbers
# string = 'ABCDE'

# characters = A  B  C  D  E
# pos index =  0  1  2  3  4
# neg index = -5 -4 -3 -2 -1
