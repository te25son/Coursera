"""
More on [R]egular [E]xpressions!
"""
#  ____  _____
# |  _ \| ____|
# | |_) |  _|
# |  _ <| |___
# |_| \_\_____|

import re # import regular expressions library

def mult_re_find(patterns, phrase):
    for p in patterns:
        print('searching for pattern {}'.format(p))
        print(re.findall(p, phrase))
        print('found {} occurences of the pattern {}'.format(len(re.findall(p, phrase)), p))
        print('\n')

#  _____ _           _      _    _ _
# |  ___(_)_ __   __| |    / \  | | |
# | |_  | | '_ \ / _` |   / _ \ | | |
# |  _| | | | | | (_| |  / ___ \| | |
# |_|   |_|_| |_|\__,_| /_/   \_\_|_|

phrase = 'sdsd..sssddd..sdddsddd...dssssss..sddddddd'

pattern1 = ['sd*'] # find an s followed by 0 or more d's
pattern2 = ['sd+'] # find all s's followed by 1 or more d's
pattern3 = ['sd?'] # find all s's followed by 0 or 1 d
pattern4 = ['sd{4}'] # find all s's followed by 4 d's ({n} can represent any number)
pattern5 = ['sd{1,3}'] # find all s's followed by 1 or 3 d's
pattern6 = ['s[sd]+'] # find all s's followed by 1 or more s or d


mult_re_find(pattern1, phrase)
mult_re_find(pattern2, phrase)
mult_re_find(pattern3, phrase)
mult_re_find(pattern4, phrase)
mult_re_find(pattern5, phrase)
mult_re_find(pattern6, phrase)

#  _____          _           _
# | ____|_  _____| |_   _  __| | ___
# |  _| \ \/ / __| | | | |/ _` |/ _ \
# | |___ >  < (__| | |_| | (_| |  __/
# |_____/_/\_\___|_|\__,_|\__,_|\___|

phrase2 = 'This is a sentence! However, it has punctunation. How can we remove it?'

pattern7 = ['[^!?.,]+'] # exclude (^) all instances of the characters '!', '?', '.', ',' that occur one or more times
pattern8 = ['[a-z]+'] # finds all instances of lowercase letter patterns
pattern9 = ['[A-Z]+'] # same but for uppercase letter patterns

mult_re_find(pattern7, phrase2)
mult_re_find(pattern8, phrase2)
mult_re_find(pattern9, phrase2)

#  ____                  _       _    ____ _
# / ___| _ __   ___  ___(_) __ _| |  / ___| |__   __ _ _ __ ___
# \___ \| '_ \ / _ \/ __| |/ _` | | | |   | '_ \ / _` | '__/ __|
#  ___) | |_) |  __/ (__| | (_| | | | |___| | | | (_| | |  \__ \
# |____/| .__/ \___|\___|_|\__,_|_|  \____|_| |_|\__,_|_|  |___/
#       |_|

phrase3 = 'Billy is 33 years old and have 22 puppies living at his house at 982 Billybo Ln, P.O. Box 2287'

pattern10 = [r'\d+'] # finds all patterns of digits
pattern11 = [r'\D+'] # finds all patterns of non-digits
pattern12 = [r'\s+'] # finds all patterns of whitespace
pattern13 = [r'\S+'] # finds all non-whitespace
pattern14 = [r'\w+'] # finds all alpha numeric patterns
pattern15 = [r'\W+'] # finds all non-alpha numeric patterns

mult_re_find(pattern10, phrase3)
mult_re_find(pattern11, phrase3)
mult_re_find(pattern12, phrase3)
mult_re_find(pattern13, phrase3)
mult_re_find(pattern14, phrase3)
mult_re_find(pattern15, phrase3)
