"""
Week 1 - Reading 1 - Formatting Strings
"""


print('')
# we can use the format function to add things into a string

first_name = 'Billy'
last_name = 'Joe'

print('My name is {} {}'.format(first_name, last_name))

print('')
# we can further make use of the format function to insert text out of order
# however, we still need to structure it.

spy1 = 'James'
spy2 = 'Bond'
print('My name is {1}, {0} {1}.'.format(spy1, spy2))

print('')

name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

print('')

num = 3.283663293
output = "{0:>10.3f} {0:>5.2f}".format(num)
print(output)

print('')

set1 = 'abc'
set2 = 'def'
set3 = 'ghi'
set4 = 'jkl'
set5 = 'mno'
set6 = 'pqr'
set7 = 'stu'
set8 = 'vwx'
set9 = 'y&z'

print("{0:>3} {8:>23}\n{1:>6} {7:>17}\n{2:>9} {6:>11}\n{3:>12} {5:>5}\n"
      "{4:>15}\n{3:>12} {5:>5}\n{2:>9} {6:>11}\n{1:>6} {7:>17}\n{0:>3} {8:>23}"
      .format(set1, set2, set3, set4, set5, set6, set7, set8, set9))
