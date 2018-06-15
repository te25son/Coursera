"""
Week 2 - Video 2 - List Searching
"""

fruits = ['banana', 'apple', 'clementine', 'orange', 'apple', 'lemon', 'pear', 'plum',
          'mango', 'banana', 'kiwi', 'apple']

# find an item in a list using the index function
print(fruits.index('clementine'))
print(fruits.index('apple'))

# you can use the 'in' operator to find items within your list
# will return a boolean value True or False
print('banana' in fruits)
print('starfruit' in fruits)
print('lemon' in fruits)

print('')

# use 'count' to count items in a list
print(fruits.count('apple'))
print(fruits.count('banana'))
print(fruits.count('kiwi'))
print(fruits.count('lime'))

print(fruits.count('apple') - fruits.count('kiwi'))

