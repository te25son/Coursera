import re

patterns = ['term1', 'term2']

text = 'this is a string with term1, but not the other'

for pattern in patterns:
    print('i\'m searching for {}'.format(pattern))

    if re.search(pattern, text):
        print('match')
    else:
        print('no match')

# or more simply

match = re.search(patterns[0], text)
print(type(match))

# get the location of the match
print(match.start())
print(text[22])  # gets first char of 'term1', i.e. 't'
