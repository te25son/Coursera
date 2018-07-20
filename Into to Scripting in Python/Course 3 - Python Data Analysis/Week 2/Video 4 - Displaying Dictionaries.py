"""
Course 3
Week 2 - Video 4 - Displaying Dictionaries
"""


def space():
    print('')


space()
HEROES_DICT = {
    'Superman': 'Clark Kent',
    'Spiderman': 'Peter Parker',
    'Batman': 'Bruce Wayne',
    'Iron Man': 'Tony Stark',
    'Hulk': 'Bruce Banner'
}


def run_dict_methods():
    """
    Runs some simple examples of dictionary methods
    """
    # these methods return an iterable object
    # similar to range()
    print('.KEYS()')
    print('-------')
    print(HEROES_DICT.keys())
    space()
    print('.VALUES()')
    print('---------')
    print(HEROES_DICT.values())
    space()
    print('.ITEMS()')
    print('--------')
    print(HEROES_DICT.items())
    space()

    # they can also be converted to lists
    print('LIST(<object>.KEYS())')
    print('---------------------')
    print(list(HEROES_DICT.keys()))
    space()
    print('LIST(<object>.VALUES())')
    print('-----------------------')
    print(list(HEROES_DICT.values()))
    space()
    print('LIST(<object>.ITEMS())')
    print('----------------------')
    print(list(HEROES_DICT.items()))  # remember this makes a list of tuples
    space()


run_dict_methods()
space()


def find_keys(my_dict):
    """
    Returns the keys of the given dictionary in string format
    """
    for key in my_dict:
        print('{} is a key'.format(key))


find_keys(HEROES_DICT)
space()


def find_values(my_dict):
    """
    Prints the values of the given dictionary in string format
    """
    for key in my_dict:
        print('{} is a value'.format(my_dict[key]))


find_values(HEROES_DICT)
space()


def find_keysandvalues(my_dict):
    """
    Prints the key and its value from the given dictionary
    """
    for key, value in my_dict.items():
        print(
            """
            \r{} is a superhero and his 
            \rsecret identity is {}.
            """.format(key, value)
        )


find_keysandvalues(HEROES_DICT)
