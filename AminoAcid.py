TRANSCRIBE_DICTIONARY = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "END", "UAG": "END",
    "UGU": "Cys", "UGC": "Cys", "UGA": "END", "UGG": "Trp",
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

AMINOACID_DICTIONARY = {
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


def translate(nucleotides):
    return TRANSCRIBE_DICTIONARY[nucleotides]


def getAminoAcid(prefix):
    # TODO: Dictionary of Protein names
    return AMINOACID_DICTIONARY[prefix]
