"""
Week 4 - Video 3 - Writing Files
"""

# to write in a file you first have to open it
# with the mode set for "write"...

openfile = open("some_file.txt", "wt")

"""
Modes for Writing
-------------------------------
w - write (erases the file first)
a - write (appends to the end of the file)
t - text (default)
b - binary
+ - open for read and write"""

print(type(openfile))
print(openfile)

openfile.close()

# now let's write to some files.
# but first...

def checkfile(filename):
    """
    Read and print the contents of a file.
    """
    datafile = open(filename, "rt")
    data = datafile.read()
    datafile.close()
    print(data)

# write...

outputfile = open("some_file.txt", "wt")

# writelines() takes a list of strings and writes them to the file
outputfile.writelines(['first line\n', 'second line\n'])

# write() takes a single string and writes the entire sting to the file
outputfile.write('third line\nfourth line\n')

outputfile.close()

checkfile('some_file.txt')

# overwrite...

outputfile2 = open("some_file.txt", "wt")
outputfile2.write("overwriting the contents\n")
outputfile2.close()

checkfile("some_file.txt")

# append...

outputfile2 = open("some_file.txt", "at")
outputfile2.write("appending to contents\n")
outputfile2.close()

checkfile("some_file.txt")
