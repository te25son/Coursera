"""
Course 3
Week 1 - Video 3 - Dictionary Lookup and Update
"""

# Learn:
# How to LOOKUP a value attached to a certain key
# How to UPDATE a value attached to a certain key


def space():
    print("")


string_keys = {
    'p': 'n', 'y': 'o', 't': 'h', 'h': 't', 'o': 'y', 'n': 'p'
}

# Use indexing with KEYS to lookup the values
print(string_keys['n'])
print(string_keys['o'])
print(string_keys['h'])
print(string_keys['t'])
print(string_keys['y'])
print(string_keys['p'])

space()


def encrypt(cipher, word):
    """
    Decrypt a word using cypher
    """
    encrypted = ""
    for char in word:
        if char not in cipher:
            continue  # doesn't break loop if char isn't in cipher
        encrypted += cipher[char]
    return encrypted


python = 'python'
print(encrypt(string_keys, python))

space()

# it is an ERROR using a non-existent key
# try the following at your own risk :-O!
# print(string_keys[1]) ---> KeyError 1

# use the GET method if you are unsure if the key exists
print(string_keys.get('t'))  # returns the value of 't' if 't' exists
print(string_keys.get(1))
print(string_keys.get('p'))
print(string_keys.get(2, 'z'))  # if first argument does not exist, returns the second
# argument, else it returns None
print(string_keys.get('o', 'z'))

space()

# modify an existing key --> value mapping
string_keys['p'] = 'r'
print(string_keys)

# this method will also CREATE a new key --> value mapping
# if the key called does not exist.
string_keys['q'] = 'k'  # adds {q: k} to the end of your dictionary
print(string_keys)

space()

print(encrypt(string_keys, python))
