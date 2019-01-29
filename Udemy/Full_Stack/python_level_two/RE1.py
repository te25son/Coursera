"""
Split strings such as emails using re
"""

import re

split_term = '@'
email = 'hello@world.com'

match = re.split(split_term, email)
print(match)

# alternative one liner
split_mail = 'johnbravo@cartoon.com'.split('@')
print(split_mail)


# find all instances!!
teacup = 'i\'m a little teacup, short and stout. here is my handle. here is my spout.'
print(re.findall('a', teacup))

count_a = len(re.findall('a', teacup))
print('there are {} a\'s in teacup'.format(count_a))
