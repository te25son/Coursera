"""
Course 3
Week 1 - Exercises
"""

import random


def space():
    print('')


# 1
my_dict = {}
print(type(my_dict))
print(my_dict)
space()

# 2
my_dict = {
    'Joe': 1,
    'Scott': 2
}
print(type(my_dict))
print(my_dict["Joe"])
print(my_dict["Scott"])
print(my_dict)
space()

# 3
my_dict['John'] = 3
print(type(my_dict))
print(my_dict["Joe"])
print(my_dict["Scott"])
print(my_dict["John"])
print(my_dict)
space()

# 4
print('Joe' in my_dict)
print('John' in my_dict)
print('Stephen' in my_dict)
space()

# 5


def is_empty(dictionary):
    """
    Given a dictionary my_dict, return True if the
    dictionary is empty and False otherwise
    """
    return len(dictionary) == 0


print(is_empty({}))
print(is_empty({0: 1}))
print(is_empty({"Joe": 1, "Scott": 2}))
space()

# 6
my_dict['Joe'] = 1
my_dict['Scott'] = 2
my_dict['John'] = 4


def value_sum(dictionary):
    """
    Given a dictionary thats values are numbers, return
    the sum of the values
    """
    fin_sum = 0
    for name in dictionary:
        if name in dictionary:
            fin_sum += dictionary[name]
        else:
            return 0
    return fin_sum


print(value_sum({}))
print(value_sum({0: 1}))
print(value_sum({"Joe": 1, "Scott": 2, "John": 4}))
space()

# 7


def make_dict(key_value_list):
    """
    Given a list of tuples of the form (key, value),
    return a dictionary with the corresponding keys and values
    """
    return dict(key_value_list)


print(make_dict([]))
print(make_dict([(0, 1)]))
print(make_dict([("Joe", 1), ("Scott", 2), ("John", 4)]))
space()

# 8
CIPHER_DICT = {
    'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c',
    'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j',
    'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z',
    'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e',
    'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a',
    't': ' ', 'w': 't'
}


def encrypt(phrase, dictionary):
    """
    Take a string phrase (lower case plus blank)
    and encypt it using the dictionary cipher_dict
    """
    encrypted = ''
    for char in phrase:
        encrypted += dictionary[char]
    return encrypted


print("Output for part 1")
print(encrypt("pig", CIPHER_DICT))
print(encrypt("hello world", CIPHER_DICT))
print()
space()

# 9


def make_decipher_dict(cipher_dict):
    """
    Take a cipher dictionary and return the cipher
    dictionary that undoes the cipher
    """
    decipher_dict = {}
    for letter in cipher_dict:
        decipher_dict[cipher_dict[letter]] = letter
    return decipher_dict


DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

print("Output for part 2")
print(DECIPHER_DICT)
print(encrypt(encrypt("pig", CIPHER_DICT), DECIPHER_DICT))
print(encrypt(encrypt("hello world", CIPHER_DICT), DECIPHER_DICT))
space()

# 10


def make_cipher_dict(alphabet):
    """
    Given a string of unique characters, compute a random
    cipher dictionary for these characters
    """
    letters = list(alphabet)
    shuffled_letters = list(alphabet)
    random.shuffle(shuffled_letters)

    cipher_dict = {}
    for idx in range(len(alphabet)):
        letter = letters[idx]
        shuffled_letter = shuffled_letters[idx]
        cipher_dict[letter] = shuffled_letter
    return cipher_dict


print("Output for part 3")
print(make_cipher_dict(""))
print(make_cipher_dict("cat"))
print(make_cipher_dict("abcdefghijklmnopqrstuvwxyz "))
