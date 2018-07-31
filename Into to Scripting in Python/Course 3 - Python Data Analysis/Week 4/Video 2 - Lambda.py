"""
Course 3
Week 4 - Video 2 - Lambda
"""

# learn anonymous functions
# ANONYMOUS FUNCTIONS = can be written in the code in one place where we need it,
# but it can never be called again because it has no name.

import random


def double_space():
    print('', '\n', '')


double_space()
data = list(range(1, 11))


def square(val):
    return val ** 2


print('my data list:')
print(data)
double_space()
print('the result of running list(map(square, data)):')
squares = list(map(square, data))
print(squares)
double_space()

# in order to use the function map() this way, we first had to define square().
# however, with LAMBDA, we don't need to define a new function.
# the following code will return the same output as above without defining a function.

print('the result of running list(map(lambda num: num ** 2, data)):')
more_squares = list(map(lambda num: num ** 2, data))
print(more_squares)
double_space()

rand_nums = [random.randrange(2, num + 3) for num in range(10)]
print('a list of random numbers:')
print(rand_nums)
double_space()
tuple_nums = list(map(lambda num1, num2: (num1, num2), data, rand_nums))
print('the result of running list(map(lambda num1, num2: (num1, num2), data, rand_nums)):')
print(tuple_nums)
double_space()

# make a list of dictionaries containing the num as the key and its square value as the value
# use lambda

square_dict = list(
    map(lambda num1, num2: {num1: num2},
        data,
        list(map(lambda num: num ** 2, data)))
)
print(square_dict)
double_space()

for dict in square_dict:
    for num in dict:
        print(dict[num])

square_dict_values = [dict[num] for dict in square_dict for num in dict]
print(square_dict_values)

double_space()
a_list = [1, '4', 9, 'a', 0, 4]

squared_ints = [e ** 2 for e in a_list if type(e) == int]

print(squared_ints)
# [ 1, 81, 0, 16 ]

a_filter = list(filter(lambda e: type(e) == int, a_list))
print('this is a filter():')
print(a_filter)
print(list(map(lambda e: e**2, filter(lambda e: type(e) == int, a_list))))

double_space()
mins = list(
    map(
        lambda pair: min(pair[0], pair[1]),
        tuple_nums
    )
)
print(mins)

# we can also use filter()
# the difference between filter() and map() is that filter doesn't necessarily
# run through and print out the entire sequence. instead, it evaluates the function
# for each element in the sequence. if the element returns as true, it adds it to
# the output list, else it does not.
print(list(filter(lambda pair: pair[1] < pair[0], tuple_nums)))