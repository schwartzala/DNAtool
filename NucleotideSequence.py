# NucleotideSequence.py
# Author: Alan Schwartz Jr.
# Last Update: 05/12/16


from Codon import translate_codon


# nucleotide_dict contains the valid nucleotides
# for each type of strand, including a blank character
# for invalid characters.
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

    # __str__ override method: returns a string of the sequence
    def __str__(self):
        return str(self.start) + "'-" + self.sequence + "-" + str(self.end) + "'"

    # complement method: finds the complementary strand
    # of "dna" or "rna". The current strand represents one
    # of the strands of the double helix structure that makes
    # up dna.
    def complement(self):
        # Check if the sequence is dna. If so, we will be converting
        # T to A and A to T.
        if self.type == "dna":
            nucleotide4 = "T"
        # Otherwise, the sequence is "rna", meaning we will be converting
        # U to A and A to U.
        else:
            nucleotide4 = "U"
        # Convert all As to a placeholder.
        self.sequence = self.sequence.replace("A", "x")
        # Convert all (T/U) to A.
        self.sequence = self.sequence.replace(nucleotide4, "A")
        # Convert all of the placeholders (previously A) to (T/U)
        self.sequence = self.sequence.replace("x", nucleotide4)
        # Convert all Cs to a placeholder.
        self.sequence = self.sequence.replace("C", "x")
        # Convert all Gs to Cs.
        self.sequence = self.sequence.replace("G", "C")
        # Convert all of the placeholders (previously C) to Gs.
        self.sequence = self.sequence.replace("x", "G")
        # Flip the start and end primes, as the complementary strand
        # goes in the opposite direction of the sense strand.
        self.start = self.end
        if self.end == 5:
            self.end = 3
        else:
            self.end = 5
        # Perform the reverse function to make the complementary strand
        # sequence go in the same direction as the sense strand.
        self.reverse()

    # reverse method: reverses the sequence
    def reverse(self):
        # Reassigns the sequence in reverse, completely reversing the
        # order of all characters in the sequence.
        self.sequence = self.sequence[::-1]
        # Flip the start and end primes as the sequence now reads
        # in reverse order.
        self.start = self.end
        if self.end == 5:
            self.end = 3
        else:
            self.end = 5

    # to_rna method: if sequence is "dna", will convert
    # the sequence to "rna"
    def to_rna(self):
        if self.type == "dna":
            self.sequence = self.sequence.replace("T", "U")
            self.type = "rna"

    # to_dna method: if sequence is "rna", will convert
    # the sequence to "dna"
    def to_dna(self):
        if self.type == "rna":
            self.sequence = self.sequence.replace("U", "T")
            self.type = "dna"

    # print_protein method: sequence takes a reading frame
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
            if frame in [0, 1, 2]:
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
                if frame + 2 >= len(self.sequence):
                    print "Frame", str(frame + 1), "\nDoes not exist. Sequence is too small.\n"
                    return
                for index in range(frame, len(self.sequence) - 2, 3):
                    # Take 3 characters starting at the current index and make them into a String.
                    codon = self.sequence[index:index+3]
                    # translate_codon method: See Codon.py
                    amino_acid = translate_codon(codon)
                    # Check to see if current amino acid is Methionine.
                    # If it is, and reading is currently False, we are now
                    # in an open reading frame. We enable highlighting using
                    # the ansi code in our protein sequence.
                    if amino_acid is "M" and reading is False:
                        reading = True
                        protein = protein + highlight
                    else:
                        # Check to see if current amino acid is a Stop codon.
                        # If it is, and reading is currently True, we are no
                        # longer in an open reading frame. We disable highlighting
                        # using the ansi code in our protein sequence.
                        if amino_acid is "*" and reading is True:
                            reading = False
                            protein = protein + unhighlight
                    # Append the current amino acid onto the protein chain.
                    protein = protein + amino_acid
                # Notify the user of the current reading frame.
                print "Frame", str(frame + 1)
                # Print out the protein sequence. Append an unhighlight ansi code
                # in case the protein ended with an open reading frame.
                print protein + unhighlight + "\n"
                return
            # If not a valid number, inform the user that they must use a valid index.
            else:
                print "Invalid reading frame! Reading frame must be of index 0, 1, or 2."
        # If an exception is raised, inform the user that the reading frame is not an integer.
        except ValueError:
            print "Could not convert frame \"" + frame + "\" into an integer."
