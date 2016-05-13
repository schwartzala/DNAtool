# Driver.py
# Author: Alan Schwartz Jr.
# Last Update: 05/12/16


from FileHandler import *
from NucleotideSequence import NucleotideSequence


# help prompt that shows command usage.
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
        run = False
    else:
        # If "h" or "help", show help prompt.
        if command == "h" or command == "help":
            print_help()
        else:
            # If "l" or "load", prompt user to entire file location.
            if command == "l" or command == "load":
                file_loc = str(raw_input("Please enter the location of your DNA / RNA sequence file (.txt):\n" +
                                         "EXAMPLES: data/maoa.txt , data/maoa_fasta.txt , "
                                         "data/maoa_rna.txt , data/short_dna.txt\n"))
                # If extension of file_loc is ".txt", perform the check_file function to make sure
                # file exists and is visible.
                if file_loc[len(file_loc) - 4: len(file_loc)].lower() == ".txt":
                    # check_file method: See FileHandler.py
                    if check_file(file_loc):
                        # NucleotideSequence object: See NucleotideSequence.py
                        # concat_lines method: See FileHandler.py
                        seq = NucleotideSequence(concat_lines(file_loc))
                        if seq.sequence is not "":
                            # Print out the sequence that was found.
                            # Perform a nested loop. The outer loop occurs twice. This is to ensure that
                            # the inner loop is performed on both the NucleotideSequence that was entered
                            # and its complement (which is obtained using the complement and reverse function
                            # of the NucleotideSequence object).
                            print "Sense Strand:", str(seq) + "\n"
                            for x in [0, 1]:
                                # Inner loop is performing the print_protein function of the NucleotideSequence
                                # object. This function takes the start index of the reading frame and proceeds
                                # to translate the sequence into a string of amino acids. This loop ensures
                                # that all three reading frames are observed and reported.
                                for frame in [0, 1, 2]:
                                    # print_protein method: see NucleotideSequence.py
                                    seq.print_protein(frame)
                                # If this is the first run, we need to also look at the complementary strand.
                                if x == 0:
                                    # complement method: see NucleotideSequence.py
                                    seq.complement()
                                    print "Complementary Strand:", str(seq)
                                print
                else:
                    # If extension of file_loc is NOT ".txt", warn the user and cancel the operation.
                    print "\"" + file_loc + "\" is not a valid file! File must have extension: \".txt\""
            # If command is not valid, inform the user and request another input.
            else:
                print command, "is not a valid command! Please use one of the following:"
                print_help()
# Thanks for using the application!
print "See you later! o/"
