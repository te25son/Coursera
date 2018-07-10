"""
Final Project for Course 2
"""


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    min_strlen = min(len(line1), len(line2))
    for item in range(min_strlen):
        if line1[item] != line2[item]:
            return item

    if min_strlen == len(line1) and min_strlen == len(line2):
        return 'IDENTICAL'

    return min_strlen


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if ('\n' or '\r') in (line1 or line2):
        return ''

    if singleline_diff(line1, line2) != 'IDENTICAL':
        if (idx < 0) or (idx > max(len(line1), len(line2))):
            return ''

        diff_num = singleline_diff(line1, line2)
        return (line1
                + '\n'
                + '=' * (diff_num)
                + '^'
                + '\n'
                + line2)

    return (line1
            + '\n'
            + 'IDENTICAL'
            + '\n'
            + line2)




thingy = "this is a line with a \n in it \n haha!"
other_thingy = "this is a line without a \\n in it \\n haha "

stringy = 'abcdefghijklmnop'
stringy2 = 'abcdefghijklmnop'

print(singleline_diff_format(thingy, other_thingy, 55))
print(singleline_diff_format(stringy, stringy2, singleline_diff(stringy, stringy2)))
