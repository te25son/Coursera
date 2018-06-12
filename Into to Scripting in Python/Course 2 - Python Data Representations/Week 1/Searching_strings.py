"""
Week 1 - Video 3 - Searching Strings
"""

print('')
sentence = 'If I wanted to find a weird thing' + \
    'that I left behind while I was working ' + \
    'on another thing, something that didn\'t occur to ' + \
    'me at the time, where would I begin to find this thing?'

print(sentence)
print('')

find_to = sentence.find('to')
print(find_to)
print(type(find_to))
# because find returns an integer, you can use it to print the 'to' it found, like so...
print(sentence[find_to], sentence[find_to + 1])

# you can also use 'rfind' to locate the LAST 'to' in your sentence
find_last_to = sentence.rfind('to')
print(find_last_to)
print(sentence[158], sentence[159])

print('')

# you can also use the built-in function 'index' and 'rindex' to find words in your sentence.
index_to = sentence.index('to')
print(index_to)
index_last_to = sentence.rindex('to')
print(index_last_to)
print(index_to - find_to)
print(index_last_to - find_last_to)

print('')

# what's the difference between INDEX and FIND?
# FIND = will look for the instance of its parameter, and if the parameter cannot be found,
# it will return a NEGATIVE NUMBER. For example...
find_tim = sentence.find('Tim')
print(find_tim)

# INDEX = will try to index the instance of its parameter, but if it doesn't find it, will
# return an error message. Try running the following code if you're so bold...
# index_tim = sentence.index('Tim')
# print(index_tim)

print('')

# we can also use the function COUNT to count the number of times a string occurs in a string.
num_of_apples = sentence.count('apple')
num_of_things = sentence.count('thing')
print('Number of apples: %s' % str(num_of_apples))
print('Number of things: %s' % str(num_of_things))  # also finds some'thing'

print('')

# we can also check to see what a string starts with and ends with using
# the built-in functions STARTSWITH and ENDSWITH. This will return the boolean
# values TRUE and FALSE.

print(sentence.startswith('I'))
print(sentence.endswith('The End'))
