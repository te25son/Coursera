"""
Week 4 - Video 1 - Opening and Reading Files in Python

NOTE:
    The instructor in this lecture ignores this issue of really knowing where the files are
    located. For now, they are giving examples using files located in the same directory as
    the Python program.
"""

openfile = open("/Users/timothyeason/Desktop/Test/grizzly_bear.txt", "rt")
# specifies the document to open and the mode to open it

# Modes for reading text.
# r = read
# t = text
# b = binary

# note: you can't have both t & b in the mode string

print(type(openfile))
print(openfile)
# this calls the file object, NOT the contents of the object.

# remember to always close the file unless you want bad things to happen to you.
openfile.close()

print('')

# now what if we want to read the contents of the file?
# remember that files are an object so we can run certain methods on them just like lists, etc.

datafile = open("/Users/timothyeason/Desktop/Test/grizzly_bear.txt", "rt")
data = datafile.read()
print('')
print(type(data))
print(len(data))

print(data)

datafile.close()
