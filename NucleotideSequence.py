# nucleotide_dict contains the valid nucleotides
# for each type of strand, including a blank character
# for invalid characters.
from codon import translate_codon

nucleotide_dict = {
    "dna": ["A", "T", "C", "G", "-"],
    "rna": ["A", "U", "C", "G", "-"]
}


# Sequence class stores DNA and RNA sequences
# along with their current strand type ("dna" or
# "rna") and the start and end of the sequence
# (5 or 3).
class NucleotideSequence:
    # Sequence of "dna" or "rna" characters
    sequence = ""
    # Strand type: "dna" or "rna"
    strand_type = ""
    # Start of sequence: 5 or 3
    start = 0
    # Start of sequence: 5 or 3
    end = 0

    # init method: instantiates the class using a
    # single parameter, sequence, which should
    # be a "dna" or "rna" sequence.
    def __init__(self, sequence):
        sequence = str(sequence).upper()
        # Check to make sure sequence isn't erroneous
        if len(sequence) < 3:
            print "Invalid sequence:", sequence
            print "Sequence must be at least 3 nucleotides long.\n"
            return
        # Check to see if sequence contains "rna" signature "U"
        if "U" not in sequence:
            self.type = "dna"
        else:
            # Check to see if sequence accidentally contains both
            # "dna" signature T and "rna" signature "U"
            if "T" in sequence:
                print "Invalid sequence:", sequence
                print "DNA Sequences only contain ATCG"
                print "RNA Sequences only contain AUCG"
                return
            self.type = "rna"
        # Make invalid characters empty character "-"
        for letter in sequence:
            if letter not in nucleotide_dict[self.type]:
                sequence = sequence.replace(letter, "-")
        self.sequence = sequence
        self.start = 5
        self.end = 3

    # toString method: returns a string of the sequence
    def __str__(self):
        return str(self.start) + "'-" + self.sequence + "-" + str(self.end) + "'"

    # reverse method: reverses the sequence
    def reverse(self):
        self.sequence = self.sequence[::-1]
        self.start = self.end
        if self.end == 5:
            self.end = 3
        else:
            self.end = 5

    # complement method: finds the complementary strand
    # of "dna" or "rna"
    def complement(self):
        if self.type == "dna":
            nucleotide4 = "T"
        else:
            nucleotide4 = "U"
        self.sequence = self.sequence.replace("A", "x")
        self.sequence = self.sequence.replace(nucleotide4, "A")
        self.sequence = self.sequence.replace("x", nucleotide4)
        self.sequence = self.sequence.replace("C", "x")
        self.sequence = self.sequence.replace("G", "C")
        self.sequence = self.sequence.replace("x", "G")
        self.start = self.end
        if self.end == 5:
            self.end = 3
        else:
            self.start = 5
        self.reverse()

    # toRNA method: if sequence is "dna", will convert
    # the sequence to "rna"
    def to_rna(self):
        if self.type == "dna":
            self.sequence = self.sequence.replace("T", "U")
            self.type = "rna"

    # toDNA method: if sequence is "rna", will convert
    # the sequence to "dna"
    def to_dna(self):
        if self.type == "rna":
            self.sequence = self.sequence.replace("U", "T")
            self.type = "dna"

    # toProtein method: sequence takes a reading frame
    # of index 0, 1, or 2.
    def print_protein(self, frame):
        # If Sequence is of type "dna", it must be converted
        # into type "rna" before being translated.
        if self.type is "dna":
            self.to_rna()
        # Convert frame into an integer.
        try:
            frame = int(frame)
            # Check if frame is a valid number (0, 1, 2). If valid, return
            # a ProteinSequence object generated from the NucleotideSequence
            # at the specified starting frame.
            if frame >= 0 or frame <= 2:
                # protein String contains the list of amino acids translated from
                # the sequence.
                protein = ""
                # reading boolean keeps track of whether or not the current codon
                # is located in a reading frame.
                reading = False
                # ansi colors are used for printing highlighted color in the terminal.
                # NOTE: Only works for Unix-based systems.
                highlight = '\033[94m'  # ansi for blue text
                unhighlight = '\033[0m'  # ansi for regular text
                # We examine each codon, which is a set of three characters in the sequence.
                # We start at the initial index of the reading frame that was passed in
                # to the function. We then go as long as there are 3 characters to be
                # read in. Finally, the 3 represents the step, since we want to skip ahead
                # 3 characters each time we examine a codon.
                for index in range(frame, len(self.sequence) - 2, 3):
                    # Take 3 characters starting at the current index and make them into a String.
                    codon = self.sequence[index:index+3]
                    # translate_codon method: See codon.py
                    amino_acid = translate_codon(codon)

                    if amino_acid is "M" and reading is False:
                        reading = True
                        protein = protein + highlight
                    else:
                        if amino_acid is "*" and reading is True:
                            reading = False
                            protein = protein + unhighlight
                    #   if reading == False:
                    #       amino_acid = amino_acid.lower()
                    protein = protein + amino_acid
                print "Frame", str(frame + 1)
                print protein + unhighlight + "\n"
            # If not a valid number, inform the user that they must use a valid index.
            else:
                print "Invalid reading frame! Reading frame must be of index 0, 1, or 2."
        # If an exception is raised, inform the user that the reading frame number is invalid.
        except ValueError:
            print "Could not convert frame \"" + frame + "\" into an integer."
