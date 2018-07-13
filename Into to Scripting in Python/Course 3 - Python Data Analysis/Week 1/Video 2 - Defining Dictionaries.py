"""
Course 3
Week 1 - Video 2 - Defining Dictionaries
"""

# use curly braces {} to indicate you want to create a dictionary


def space():
    print('')


print("This is an empty dictionary:")
empty_dict = {}
print(empty_dict)

space()

print("""This is a simple dictionary where the 
key = 1 and the value of the key = 2:""")
one_two = {1: 2}
print(one_two)

space()

# we can add more than one key value to a dictionary
print("A dictionary containing the square value of its key:")
square_values = {
    1: 1, 2: 4, 3: 9, 4: 16
}
print(square_values)

space()

print("And here's a dictionary with keys and values being strings:")
string_keys = {
    'p': 'n', 'y': 'o', 't': 'h', 'h': 't', 'o': 'y', 'n': 'p'
}
print(string_keys)

space()

# keys and values DO NOT have to have the same value as each other

print('A dictionary with boolean values and string keys:')
easy_languages = {
    'Italian': True, 'Russian': False
}
print(easy_languages)

space()

print("""And here is a dictionary where the key is a string
and the value is a list:""")
biggest_cities = {
    'China': ['Shanghai', 'Beijing'],
    'USA': ['New York', 'Las Angeles'],
    'Spain': ['Madrid', 'Barcelona'],
    'Australia': ['Sydney', 'Melbourne'],
    'Texas': ['Houston', 'San Antonio']
}
print(biggest_cities)

space()

# we can also create dictionaries using the DICT function

print("Here is an empty dictionary created using the dict() function:")
empty_dict2 = dict()
print(empty_dict2)

space()

print("This is a list:")
a_list = [(1, 'one'), (2, 'two'), (3, 'three')]
print(a_list)
print("And this is a dictionary of that list:")
print(dict(a_list))

space()

# we can also "copy" dictionaries using the DICT function

print("This is a copy of biggest_cities using the dict() function:")
biggest_citiescopy = dict(biggest_cities)
print(biggest_citiescopy)
