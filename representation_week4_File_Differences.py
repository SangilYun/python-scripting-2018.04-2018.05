"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1


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
    if len(line1) > len(line2) :
        shortline = line2
        longline = line1
    else :
        shortline = line1
        longline = line2

    for dummy_i in range(len(longline)) :
        if dummy_i < len(shortline) :
            if shortline[dummy_i] != longline[dummy_i] :
                return dummy_i
        elif dummy_i >= len(shortline):
            return dummy_i

    return IDENTICAL

# print("===")
# print(singleline_diff("","1"))
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
    if len(line1) > len(line2) :
        shortline = line2
    else :
        shortline = line1

    return_str = ""

    if (idx >=0) and (0 <= idx <= len(shortline)):
        # if idx == index :
        indicator = "\n"+(idx) * "=" + "^\n"
        return_str += line1 + indicator + line2+ "\n"



    return return_str

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
    if len(lines1) > len(lines2) :
        shortlines = lines2
        longlines = lines1
    else :
        shortlines = lines1
        longlines = lines2
    answer = [IDENTICAL, IDENTICAL]
    for dummy_i in range(len(longlines)):
        if dummy_i <len(shortlines):
            index = singleline_diff(lines1[dummy_i], lines2[dummy_i])

            if index != IDENTICAL :
                answer[0] = dummy_i
                answer[1] = index
                break
        else :
            answer[0] = dummy_i
            answer[1] = 0
            break


    return tuple(answer)


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
    openfile = open(filename, "rt")
    file = openfile.read()
    splitfile = file.split("\n")
    lst = filter(None, splitfile)
    openfile.close()
    return lst

# print(get_file_lines("untitled.txt"))

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
    return_str = ""
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    # print(lines1)
    # print(lines2)
    # print(lines1[0])
    # print(lines2[0])
    line = multiline_diff(lines1, lines2)
    # print("line :", line)
    # print("line[0] :", line[0])
    # print("lines1[line[0]] :", lines1[line[0]])
    # print("lines2[line[0]] :", lines2[line[0]])

    if line != (IDENTICAL, IDENTICAL) :
        return_str += "Line " + str(line[0]) +":\n" + \
        singleline_diff_format(lines1[line[0]], lines2[line[0]], line[1])
        return return_str
    else :
        return_str += "No differences\n"
    return return_str


# Line 0:
# abc
# ^

# print(file_diff_format('untitled.txt', 'untitled 2.txt'))
# lines1 = get_file_lines("untitled.txt")
# lines2 = get_file_lines("untitled 2.txt")
# print("lines1 :", get_file_lines("untitled.txt"))
# print("lines2 :",get_file_lines("untitled 2.txt"))
# print("line :", multiline_diff(lines1, lines2))
#
# print(file_diff_format("untitled.txt", "untitled 2.txt"))
