"""
This is very unnecessary as I'm most comfortable with Python, but what the heck...
Best to know the basics very well
"""

print("hello world!")

# this is an integer (int)
a = 10
print(type(a))

# this is a float
b = 10.0
print(type(b))

# this is a string (str)
string = "hi there"
print(type(string))

# this is a boolean (bool)
boo = True
boo2 = False

print(type(boo))
print(type(boo2))

# for loop
for char in string:
    print(char)

# while loop
while boo:  # means while boo is true
    print("hello" * 100)
    boo = False  # this will end the loop b/c the while condition will no longer be true

# conditions
if boo:
    print("boo is true")
else:
    print("boo is false")

if not boo2:
    print("boo2 is false")
else:
    print("boo2 is true")

boo = True

# index slicing with a for loop
for i in range(len(string)):
    print(string[i])

# three ways of indexing
# 1 - grab the specific index you want
one = string[0]  # gets the first character in the string
print(one)

# 2 - grab a specific section of an array/list/string/whathaveyou
two = string[1:5]  # grabs the second up to BUT NOT INCLUDING the 5th character
print(two)

# 3 - grab a specific section of an array and define the step
three = string[1:5:2]  # starts at the second element, skips the following element, gets the element after that, and repeats up to but not including the 5th element
print(three)
