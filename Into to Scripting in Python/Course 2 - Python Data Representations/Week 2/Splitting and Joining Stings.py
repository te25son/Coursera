"""
Week 2 - Video 3 - Splitting and Joining Strings
"""

print('')

poem = """The Grizzly bear is huge it wild, 
he has devoured the infant child, 
The infant child is not aware, 
it has been eaten by the bear.
"""

print(poem)

print('')

words = poem.split()
print(words)
# note that the above function "split" only splits where it "sees" whitespace.
# for further clarification look where there is punctuation.

print(poem.find('wild'))
print(poem[28:33])
print(words[6])

print('')

# HOWEVER, you can call split with an argument to fix this (kind of)
words2 = poem.split(" ")  # argument tells the function to split the word whenever there is a space
# in this particular case it doesn't do much, but you can move the words around to make it really do something.
print(words2)
print(words[-1])
print(words2[-1])

print('')

# OR you can pass it a different argument
phrase = poem.split(",")
print(phrase)
new_line = poem.split('\n')
print(new_line)

print('')

for i in range(len(new_line) - 1):
    print(new_line[i])

print('')

# THE ARGUMENTS ARE ENDLESS!!!
split_is = poem.split('is')
print(split_is)

print('')

print(split_is[0])
print(split_is[1])
print(split_is[2])

# NOTICE what you put to the argument is NOT included in the created list

vowels = poem.split('a', 1)
# this tells the function to split at the first instance of 'a' and that's all
# if you wrote '2', it would split at the first 2 instances of 'a',
# 3, the first 3, and so on.
print(vowels[-1])
vowels2 = poem.split('a', 2)
print(vowels2[-1])
vowels3 = poem.split('a', 3)
print(vowels3[-1])

# We can also JOIN strings back together.
items = ['cups', 'mugs', 'spoons', 'flowers', 'vase', 'car', 'laptop']
print(items)

print('')

# use the function '.join' to join strings together.
# NOTE that it will not join lists together, so you must use it on strings.
# example...
print(''.join(items))  # the initial string tells the function what you want to join BETWEEN the items
print(' '.join(items))
print(', '.join(items))
