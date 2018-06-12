"""
Week 1 - Video 4 - Slicing Strings
"""

word = 'everything'

print(word[1:5])  # begins at index 1 up to, but not including index 5
print(word[5:9])  # begins at index 5 up to, but not including index 9

print('')

# we can also use this formula to make open-ended slices. for example...
print(word[5:])
print(word[:4])

print('')

print('This is the %s best %s %s' % (word[1:5], word[5:], word[:4]))

print('')

# remember that we can also use NEGATIVE indices.
print(word[-3:])  # this should give me the last three characters in the string
print(word[2:-3])  # and this should give me from 2 up to, but not including the 3rd from last character

print('')

# we can also go past the total number of characters in a string.
# However, this will return nothing
print('$' + word[22:70] + 'pp')  # there's no space becuase there is NOTHING there
print(word[8:100])  # this will give me everything from 8 to the end

"""
Tip: think of strings in this case as being infinite. You can call the index of any part of 
the string, but note that it won't always be there. In some cases, it will return nothing.
"""

# we can further return NOTHING from a string in the following ways
print(word[6:6])
print(word[4:2])
