codon_dict = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
    "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

prefix_dict = {
    "Phe": "Phenylalanine",
    "Leu": "Leucine",
    "Ser": "Serine",
    "Tyr": "Tyrosine",
    "END": "Stop Codon",
    "Cys": "Cysteine",
    "Trp": "Tryptophan",
    "Pro": "Proline",
    "His": "Histidine",
    "Gln": "Glutamine",
    "Arg": "Arginine",
    "Ile": "Isoleucine",
    "Met": "Methionine",
    "Thr": "Threonine",
    "Asn": "Aspargine",
    "Lys": "Lysine",
    "Val": "Valine",
    "Ala": "Alanine",
    "Asp": "Asparagine",
    "Glu": "Glutamine",
    "Gly": "Glycine"
}


def translate_codon(codon):
    if type(codon) != str:
        print "invalid input:", codon
        print "codon must be of type str"
        return
    if len(codon) != 3:
        print "invalid input:", codon
        print "codon must be of length 3"
        return
    if codon not in codon_dict:
        print "invalid input:", codon
        print "codon must be present in codon_dict"
        return
    return codon_dict[codon]


def get_amino_acid(prefix):
    if type(prefix) != str:
        print "invalid input:", prefix
        print "prefix must be of type str"
        return
    if len(prefix) != 3:
        print "invalid input:", prefix
        print "prefix must be of length 3"
        return
    if prefix not in prefix_dict:
        print "invalid input:", prefix
        print "prefix must be present in prefix_dict"
        return
    return prefix_dict(prefix)
