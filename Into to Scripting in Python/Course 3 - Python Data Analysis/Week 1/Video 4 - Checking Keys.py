"""
Course 3
Week 1 - Video 4 - Checking Keys
"""

# Learn:
# How to determine if a key is actually mapped in the dictionary
# How to protect yourself if you're unsure about a key being in the dictionary


def space():
    print('')


my_map = {
    1: 5, -3: 45, 15: 2, -400: 0, 0: 67
}

my_other_map = {
    'hello': 'goodbye',
    'coffee': 'tea',
    'food': 'drink',
    'breakfast': 'dinner',
    'goodbye': 'hello'
}

# we can use the IN operator to determine if a key is in a mapping
print(1 in my_map)
print(-400 in my_map)
print(90 in my_map)
print('hello' in my_other_map)
print('breakfast' in my_other_map)
print('yellow' in my_other_map)

space()

# NOTE the in operator only works when finding KEYS in maps, NOT values
print(45 in my_map)
print(5 in my_map)
print('drink' in my_other_map)
print('dinner' in my_other_map)

space()

# what about something that is both a key AND a value?
print(0 in my_map)
print('hello' in my_other_map)

space()

# and if it's neither a key nor value...
print(90 in my_map)
print('ice cream' in my_other_map)

space()

# Now, how do we protect ourselves when looking through a dictionary?
keys = [1, 7, 15, 22, 0]

for key in keys:
    if key not in my_map:
        continue
    print(key, ':', my_map[key])

# OR (more simply)

for key in keys:
    if key in my_map:
        print(key, ':', my_map[key])

space()

# issues with Keys
# NOTE: it is recommended that you make all keys the same TYPE
crazy_map = {
    4.0: 'z', True: 'true', 'a': 3, False: 0, 15: 'k'
}

# for example weird things will happen like this...
crazy_map[1] = 7
print(crazy_map)
# and this...
crazy_map[0] = 'such a mess!'
print(crazy_map)
# You would think that because 1 and 0 are not keys in the dictionary
# that this would add a new mapping to the existing dictionary.
# However, 1 and 0 are built-in references to True and False respectively.
# Therefore, we changed the values of the existing keys True and False.
crazy_map[4] = '??'  # --> still no despite being an int rather than a float
print(crazy_map)
crazy_map['A'] = 'xyz'  # --> will work because Python is CASE SENSITIVE
print(crazy_map)
