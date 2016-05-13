# check_file method checks to see if file location is valid. If so, it returns True. Otherwise, it returns False.
def check_file(file_loc):
    try:
        open(file_loc)
    except IOError:
        print "\"" + file_loc + "\" is not a valid file location! File could not be found."
        return False
    return True


# concat_lines method takes all lines in a file and concatenates them into a single String.
def concat_lines(file_loc):
    big_line = ""
    with open(file_loc) as f:
        for line in f:
            line = line.replace('\n', '')
            big_line = big_line + line
    return big_line