"""
Iterating over files.
---------------------

readlines gives back a list of strings
each string in this list coresponds to a single
line in the file.

How do we use it?"""

Start by opening the file.

datafile = open("some_text.txt", "rt")

for line in datafile.readlines():
    print(line)

datafile.close()

"""
In some cases you may find datafile will be too slow. 
After all, because readlines() reads through a whole text
then breaks it up into a list of strings corresponding to 
each line of the text, this could take a while. The
function also takes up quite a bit of memory, especially
it the file is large. 

Luckily, Python offers us a way to more quickly complete this
function."""

datafile2 = open("some_text.txt", "rt")

for line in datafile2:
    print(line)

datafile2.close()

"""
This will do the same thing as readfile(), 
but instead of reading it all at once and storing it
in a huge list, it will just iterate over everything 
that's already there without storing it in another
location first.

Normally when working with files, you'll want to work with 
it line-by-line rather than as one big string."""
