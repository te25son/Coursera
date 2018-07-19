"""
Course 3
Week 2 - Video 1 - Iteration Over Dictionaries
"""


def space():
    print('')


space()

heroes_villains = {
    'Batman': 'Joker',
    'Superman': 'Lex Luther',
    'X-Men': 'Magneto',
    'Thor': 'Loki',
    'Avengers': 'Thanos'
}

for heroes in heroes_villains:
    print('%s vs. %s' % (heroes_villains[heroes], heroes))

space()

# we can also print directly over the keys using the key() function
# but this effectively does the same as above
for heroes in heroes_villains.keys():
    print('%s vs. %s' % (heroes_villains[heroes], heroes))

space()

# here's an example of the key() function at work...
super_keys = heroes_villains.keys()
print(super_keys)

space()

# we can also iterate over the values of a dict. using the values() function
# NOTE: this WILL NOT be in any particular order. it randomizes the list.
for villain in heroes_villains.values():
    print('{} is a villain!'.format(villain))

space()

evil_values = heroes_villains.values()
print(evil_values)

space()

# we can also use the function items() which returns a list of tuples
# here's an example...
super_tuple_list = heroes_villains.items()
print(super_tuple_list)

space()

# and, of course, we can iterate over this as well...
for hero, villain in super_tuple_list:
    print('{} is the villain in {}.'.format(villain, hero))

space()

# furthermore, we can use the IN operator to check if something is... in... our dictionary
# NOTE: in will by default check if the item you're looking for is a key, not a value

print('Spiderman' in heroes_villains)
print('Batman' in heroes_villains)

# we can be more specific by using the key() function
print('Aquaman' in heroes_villains.keys())
print('Avengers' in heroes_villains.keys())

# it is possible to check the values in the dictionary using in
# by using the values() function
print('Ultron' in heroes_villains.values())
print('Thanos' in heroes_villains.values())
