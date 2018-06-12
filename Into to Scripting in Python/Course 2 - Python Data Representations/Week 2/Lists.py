"""
Week 2 - Video 1 - Lists
"""

# lists are created using []
empty = []
print(empty)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

languages = ['python', 'javascript', 'c++', 'haskell', 'lisp']
print(languages)

# python allows you to mix types in a list,
# but you are STRONGLY advised NOT to do this.
mixed_list = ['hello', 10, True]
print(mixed_list)

print('')

# you can also create a list using the 'list' function
mylist = list()
print(mylist)

seq = range(5)  # tells python to make a range of digits from 0 up to but not including 5
print(seq)  # printing this out will tell you it's a range from what to what, but doesn't give all the digits

seq_list = list(seq)  # but when you put this range into a list, all the digits show up
print(seq_list)

seq2 = range(7, 15)
print(seq2, list(seq2))

# you can also put 3 parameters to the range function
seq3 = range(4, 39, 5)
# this tells python to start at four and increase by 5 each time up to, but not
# including 39
print(list(seq3))

# furthermore, we can use negative numbers
seq4 = range(10, 2, -1)
print(list(seq4))
