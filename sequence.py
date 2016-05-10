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
class Sequence:
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
        # Check to make sure sequence isn't erroneous
        if len(sequence) < 3:
            print "invalid input:", sequence
            print "sequence must be at least 3 nucleotides long"
            return
        # Check to see if sequence contains "rna" signature "U"
        if "U" not in sequence:
            self.type = "dna"
        else:
            # Check to see if sequence accidentally contains both
            # "dna" signature T and "rna" signature "U"
            if "T" in sequence:
                print "invalid input", sequence
                print "dna sequence must contain ATCG"
                print "rna sequence must contain AUCG"
                return
            self.type = "rna"
        # Make invalid characters empty character "-"
        for letter in sequence:
            if letter not in nucleotide_dict[self.type]:
                sequence = sequence.replace(letter, "-")
        self.sequence = sequence
        self.start = 5
        self.end = 3
        return self

    # toString method: returns a string of the sequence
    def __toString__(self):
        return self.start + "'-" + self.sequence + "-" + self.DNASequence.end + "'"

    # reverse method: reverses the sequence
    def __reverse__(self):
        self.sequence = self.sequence[len(self.sequence)-1:0:-1]
        self.start = self.end
        if self.end == 5:
            self.end = 3
        else:
            self.end = 5

    # complement method: finds the complementary strand
    # of "dna" or "rna"
    def __complement__(self):
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
        self.reverse()

    # toRNA method: if sequence is "dna", will convert
    # the sequence to "rna"
    def __toRNA__(self):
        if self.type == "dna":
            self.sequence = self.sequence.replace("T", "U")
            self.type = "rna"

    # toDNA method: if sequence is "rna", will convert
    # the sequence to "dna"
    def __toDNA__(self):
        if self.type == "rna":
            self.sequence = self.sequence.replace("U", "T")
            self.type = "dna"