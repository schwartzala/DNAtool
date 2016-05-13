# help prompt that shows command usage.
from file_handler import *
from NucleotideSequence import NucleotideSequence


def print_help():
    print "[L]oad: Import a DNA or RNA sequence from file"
    print "[H]elp: Prompt usage script"
    print "[E]xit: Exit the program\n"

# run flag is used to see if the user wishes to continue using the application.
run = True
# show help prompt at the beginning for new users
print_help()
while run:
    # Request user to input a command.
    command = str(raw_input("Please enter a command: [L]oad / [H]elp / [E]xit\n")).lower()
    # If "e" or "exit", exit the program.
    if command == "e" or command == "exit":
        print "See you later! o/"
        run = False
    else:
        # If "h" or "help", show help prompt.
        if command == "h" or command == "help":
            print_help()
        else:
            # If "l" or "load", prompt user to entire file location.
            if command == "l" or command == "load":
                file_loc = str(raw_input("Please enter the location of your DNA / RNA sequence file: "))
                # If extension of fileLoc is ".txt", perform the check_file function to make sure
                # file exists and is visible.
                if file_loc[len(file_loc) - 4: len(file_loc)] == ".txt":
                    # check_file method: See file_handler.py
                    if check_file(file_loc):
                        # NucleotideSequence object: See NucleotideSequence.py
                        seq = NucleotideSequence(concat_lines(file_loc))
                        # Perform a nested loop. The outer loop occurs twice. This is the ensure that
                        # the inner loop is performed on both the NucleotideSequence that was entered
                        # and its complement (which is obtained using the complement and reverse function
                        # of the NucleotideSequence object).
                        print "Sense Strand\n"
                        for x in range(0, 2):
                            for frame in range(0, 3):
                                seq.print_protein(frame)
                            # If this is the first run, we need to also look at the complementary strand.
                            if x == 0:
                                # This returns the reverse complement of the NucleotideSequence, ensuring
                                # that our sequence is properly translated from 5' to 3'.
                                seq.complement()
                                print "Complementary Strand"
                            print
                else:
                    # If extension of fileLoc is NOT ".txt", warn the user and cancel the operation.
                    print "\"" + file_loc + "\" is not a valid file! File must have extension: \".txt\""
            # If command is not valid, inform the user and request another input.
            else:
                print command, "not a valid command! Please use one of the following:"
                print_help()
