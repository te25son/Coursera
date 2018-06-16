"""
Week 2 - Video 5 - Iteration over Lists

iteration = repeating something over and over again
"""


print('')


def print_items(a_list):
    """
    Takes a parameter (list) and prints the items in that list
    """
    for item in a_list:
        print(item)


to_do = ['feed the dog', 'pick up groceries', 'cook dinner', 'clean the bathroom',
         'fold laundry', 'finish homework']
numbers = range(0, 105, 6)

print_items(to_do)
print_items(numbers)

print('')

# the following is a bad example of a function that does that same thing as the above
# function.
# it's bad because it's prone to errors.


def do_not_use(a_list):
    """
    Iterates over a_list and prints the items within that list.
    WARNING:
        This is only to be used as an example of what NOT to do.
        DO NOT USE THIS!
    """
    length = len(a_list)
    for index in range(length):
        print(a_list[index])


do_not_use(to_do)
do_not_use(numbers)
# the function still works, but just because something works doesn't mean you should use it.
# there are more reliable ways to write this function, as we have already seen.

print('')

# we can further use iteration as a way to count the items within list
def count_items(a_list):
    """
    Counts the number of items in a list
    """
    count = 0
    for item in a_list:
        count = count + 1
    return count


print(count_items(to_do))
print(count_items(numbers))

print('')


def count_odd_numbers(numlist):
    """
    Returns the number of items in numlist
    """
    count = 0
    for num in numlist:
        if num % 2 == 1:
            count += 1
    return count


print(count_odd_numbers(numbers))
print(count_odd_numbers(range(0, 100, 3)))
print(list(range(0, 100, 3)))
