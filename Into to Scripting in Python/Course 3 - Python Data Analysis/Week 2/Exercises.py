"""
Course 3
Week 2 - Exercises!!
"""


def double_space():
    print('', '\n', '')


def question_title(num):
    """
    Takes a question number (num) and prints a
    title for the question.
    """
    title_str = 'Test for question {}'.format(num)
    print(title_str
          + '\n'
          + '-' * len(title_str))


double_space()


# 1
question_title(1)
nested_list = [
    [], [], [], [], []
]
print(nested_list)
double_space()


# 2
question_title(2)
nested_list = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(nested_list)
double_space()


# 3
question_title(3)
zero_list = [0 for x in range(3)]
print(zero_list)

nested_list = [[0 for num in range(3)] for num2 in range(5)]
print(nested_list)
double_space()


# 4
question_title(4)
# Define a nested list of lists
nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]
print(nested_list)

# Add code to print out the item in this nested list with value 7
print(nested_list[2][1])
double_space()


# 5
question_title(5)
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
    nested_list.append(zero_list)
print(nested_list)

nested_list[2][1] = 7
print(nested_list)

# In the above example, the command nested_list[2][1] changes a reference within nested_list.
# Because the reference refers also to every item in nested_list, all the items are changed.
# We can fix this simply by adding on thing...
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
    nested_list.append(list(zero_list))  # rather than calling a reference, we make a copy of the list
print(nested_list)

nested_list[2][1] = 7
print(nested_list)
double_space()

# 6
question_title(6)
list_dict = [
    {}, {}, {}, {}, {}
]
print(list_dict)
double_space()


# 7
question_title(7)


def dict_copies(my_dict, num_copies):
    """
    Given a dictionary my_dict and an integer num_copies,
    returns a list consisting of num_copies copies of my_dict.
    """
    return [dict(my_dict) for num in range(num_copies)]


print(dict_copies({}, 0))
print(dict_copies({}, 1))
print(dict_copies({}, 2))

test_dict = dict_copies({'a': 1, 'b': 2}, 2)
print(test_dict)

test_dict[1]["a"] = 3
print(test_dict)
print('')


# 8
question_title(8)


def make_dict_lists(length):
    """
    Given an integer length, returns a dictionary whose keys
    lie in range(length) and whose corresponding values are
    lists of zeros with length matching the key
    """
    return {
        num: [0 for num in range(num)] for num in range(length)
    }


print(make_dict_lists(0))
print(make_dict_lists(1))
print(make_dict_lists(5))
double_space()


# 9
question_title(9)
grade_table = {
    "Joe": [100, 98, 100, 13],
    "Scott": [75, 59, 89, 77],
    "John": [86, 84, 91, 78]
}


print(grade_table["Joe"])
print(grade_table["Scott"])
print(grade_table["John"])
double_space()


# 10
question_title(10)


def make_grade_table(name_list, grades_list):
    """
    Given a list of name_list (as strings) and a list of grades
    for each name, return a dictionary whose keys are
    the names and whose associated values are the lists of grades
    """

    return {
        name: a_list for name, a_list in zip(name_list, grades_list)
    }


print(make_grade_table([], []))

name_list = ["Joe", "Scott", "John"]
grades_list = [[100, 98, 100, 13], [75, 59, 89, 77], [86, 84, 91, 78]]
print(make_grade_table(name_list, grades_list))
