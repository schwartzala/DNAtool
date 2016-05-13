# FileHandler.py
# Author: Alan Schwartz Jr.
# Last Update: 05/12/16


# check_file method checks to see if file location is valid. If so, it returns True. Otherwise, it returns False.
def check_file(file_loc):
    # Try statement allows us to handle errors ourselves, preventing the application from crashing.
    try:
        # Open file will try to create an object from the file at file_loc.
        open(file_loc)
    # If file fails to open because it does not exist, it will cause an IOError. This allows us
    # to handle the IOError how we want to.
    except IOError:
        # Inform the user that the file was not found and send a false statement.
        print "\"" + file_loc + "\" is not a valid file location! File could not be found.\n"
        return False
    # File was found! Return true to continue the application!
    return True


# concat_lines method takes all lines in a file and concatenates them into a single String.
def concat_lines(file_loc):
    # big_line represents a large String composed of all the lines of the file.
    big_line = ""
    # Create an object called inFile that contains all of the lines of that file.
    with open(file_loc) as inFile:
        # Iterate through each line contained in inFile.
        for line in inFile:
            # In case the file is a FASTA file, skip over the line if it contains the > symbol.
            if ">" not in line:
                # Get rid of next line (\n) characters.
                line = line.replace('\n', '')
                # Trim any extra white space.
                line = line.replace(' ', '')
                # FASTA format contains a line with extra data that begins with a > symbol.
                # Append the current line that has been reformatted onto the end of the big_line
                big_line = big_line + line
    # Return the large String
    return big_line
