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


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    fin_list = []
    min_list = min(len(lines1), len(lines2))
    for item in range(min_list):
        if lines1[item] != lines2[item]:
            fin_list.append(item)
            fin_list.append(singleline_diff(lines1[item], lines2[item]))        
            return tuple(fin_list)
    
    if min_list == len(lines1) and min_list == len(lines2):
        fin_list.append('IDENTICAL')
        fin_list.append(singleline_diff(lines1[item], lines2[item]))
        return tuple(fin_list)
    
    fin_list.append(min_list)
    fin_list.append(0)
    return tuple(fin_list)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    the_list = []
    the_file = open(filename, "rt")
    for line in the_file:
        if '\n' in line:
            the_list.append(line[:-1])
    the_list.append(line)

    the_file.close()

    return the_list


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file_list1 = get_file_lines(filename1)  # makes a list of lines from filename1
    file_list2 = get_file_lines(filename2)	# makes a list of lines from filename2
    
    if file_list1 == file_list2:  # checks if the lines in each list are the same
        return 'No differences\n'
    
    first_diff = multiline_diff(file_list1, file_list2)  # creates a tuple containing the first line difference
    formated_diff = singleline_diff_format(file_list1[first_diff[0]],
                                            file_list2[first_diff[0]],
                                            first_diff[1])  # creates a formated, multi-line string displaying the location of the mismatch
    
    return ('Line %s:' % str(first_diff[0])
            + '\n'
            + formated_diff)
