# Codon.py
# AUTHOR: Alan Schwartz Jr.
# LASTUPDATE: 05/12/16


# codon_dict: map structure that contains codon keys
# and their associated amino acid values.
codon_dict = {
    "UUU": "F", "UCU": "S", "UAU": "Y", "UGU": "C",
    "UUC": "F", "UCC": "S", "UAC": "Y", "UGC": "C",
    "UUA": "L", "UCA": "S", "UAA": "*", "UGA": "*",
    "UUG": "L", "UCG": "S", "UAG": "*", "UGG": "W",
    "CUU": "L", "CCU": "P", "CAU": "H", "CGU": "R",
    "CUC": "L", "CCC": "P", "CAC": "H", "CGC": "R",
    "CUA": "L", "CCA": "P", "CAA": "Q", "CGA": "R",
    "CUG": "L", "CCG": "P", "CAG": "Q", "CGG": "R",
    "AUU": "I", "ACU": "T", "AAU": "N", "AGU": "S",
    "AUC": "I", "ACC": "T", "AAC": "N", "AGC": "S",
    "AUA": "I", "ACA": "T", "AAA": "K", "AGA": "R",
    "AUG": "M", "ACG": "T", "AAG": "K", "AGG": "R",
    "GUU": "V", "GCU": "A", "GAU": "D", "GGU": "G",
    "GUC": "V", "GCC": "A", "GAC": "D", "GGC": "G",
    "GUA": "V", "GCA": "A", "GAA": "E", "GGA": "G",
    "GUG": "V", "GCG": "A", "GAG": "E", "GGG": "G"
}


# UNUSED IN DRIVER
# prefix_dict: map structure that contains amino acid
# single character keys and their full name values.
amino_acid_dict = {
    "F": "Phenylalanine",
    "L": "Leucine",
    "S": "Serine",
    "Y": "Tyrosine",
    "*": "Stop Codon",
    "C": "Cysteine",
    "W": "Tryptophan",
    "P": "Proline",
    "H": "Histidine",
    "Q": "Glutamine",
    "R": "Arginine",
    "I": "Isoleucine",
    "M": "Methionine",
    "T": "Threonine",
    "N": "Asparagine",
    "K": "Lysine",
    "V": "Valine",
    "A": "Alanine",
    "D": "Aspartic Acid",
    "E": "Glutamic Acid",
    "G": "Glycine"
}


# translate_codon method: takes a codon and returns
# the associated amino acid value from codon_dict.
def translate_codon(codon):
    # Check to see if codon is a String.
    if type(codon) is not str:
        print "Invalid codon:", codon
        print "Codon must be of type str"
        return
    # Check to see if codon is length 3.
    if len(codon) is not 3:
        print "Invalid codon:", codon
        print "Codon must be of length 3"
        return
    # Check to see if codon is in codon_dict.
    # If not found, return a ?.
    if codon not in codon_dict:
        return "?"
    # If it is valid, return the appropriate
    # amino acid value.
    return codon_dict[codon]


# UNUSED IN DRIVER
# get_amino_acid method: takes an amino acid
# single character
def get_amino_acid(amino_acid):
    # Check to see if amino acid is a String.
    if type(amino_acid) is not str:
        print "Invalid amino acid:", amino_acid
        print "Amino acid must be of type str"
        return
    # Check to see if amino acid is length 1.
    if len(amino_acid) is not 1:
        print "Invalid amino acid:", amino_acid
        print "Amino acid must be of length 3"
        return
    # Check to see if amino acid is in amino_acid_dict.
    if amino_acid not in amino_acid_dict:
        print "Invalid amino acid:", amino_acid
        print "Amino acid must be present in prefix_dict"
        return
    # If it is valid, return the appropriate
    # amino acid full name.
    return amino_acid_dict[amino_acid]
