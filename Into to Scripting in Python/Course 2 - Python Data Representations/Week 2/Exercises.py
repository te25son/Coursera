"""
Week 2 - Exercises
"""


# 1
prime_nums = [2, 3, 5, 7, 11, 13]
print(prime_nums[1], prime_nums[3], prime_nums[5])

# 2
example_list = prime_nums
firstlast_list = [example_list[0], example_list[-1]]
print(firstlast_list)

# 3
middle_list = example_list[1:-1]
print(middle_list)

# 4
truefalse_list = [True] * 8 + [False] * 8
print(truefalse_list)

# 5
quote = 'Bring me a shrubbery'
word_list = quote.split()
print(word_list)

# 6
def word_count(text, word):
    """
    Given a string (text) consisting of words and a string (word) with no spaces,
    return the number of times 'word' appears in 'text'.
    """
    word_count = text.split(' ')
    return word_count.count(word)

print(word_count("this manbearpig is a fine manbearpig", "manbearpig"))
print(word_count("this manbearpig is not a man", "man"))
print(word_count("this manbearpig is not a pig", "pig"))
print(word_count("this manbearpig is not a bear", "bear"))

# 7
list1 = [2, 3, 5, 7, 11, 13]

list2 = list1

print(list1)
print(list2)

list2[0] = 0

print(list1)
print(list2)

# EXPLAIN WHAT HAPPENED:
# list2 is an alias of list1, so anything that happens to list1 happens to list2 and vice versa.
# Consider Batman and Bruce Wayne. They may not appear the same or have the same name, but they're
# both names that refer to the same person. So anything that happens to Batman also happens
# to Bruce Wayne.

# 8
list1 = [2, 3, 5, 7, 11, 13]

list2 = list(list1)

print(list1)
print(list2)

list2[0] = 0

print(list1)
print(list2)

# EXPLAIN WHAT HAPPENED:
# In this example, we created a new list (list2) referencing the old list (list1) using
# the list constructor. Unlike our previous example, here we have two distinct lists. Updating
# an item in one list does not affect the other list.

# 9
def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    max_num = numbers[0]
    for num in numbers[0 :]:
        if num > max_num:
            max_num = num
    return max_num

print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))

# 10
def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    final_num = ''
    for num in int_list[0 :]:
        final_num += str(num)
    return int(final_num)

print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))
