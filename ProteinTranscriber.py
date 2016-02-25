# Alan Schwartz Jr.
# Lab 4: Gene Expression

# Amino Acid Dictionary

aminoAcidDict = {
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


def clip(s):
    return s[3:len(s) - 3]


def transcribe(seq):
    aminoAcid = ""
    seq = clip(seq)
    while (len(seq) > 2):
        aminoAcid = aminoAcid + aminoAcidDict[seq[0:3]]
        if (aminoAcid[0:3] != "Met"):
            aminoAcid = ""
        if (aminoAcid[len(aminoAcid) - 3:len(aminoAcid)] == "END"):
            return aminoAcid
        seq = seq[3:]
    return aminoAcid


def checkExonIntron(seq):
    editseq = ""
    exon = True
    while len(seq) > 0:
        if seq[0] == "i":
            exon = False
        else:
            if seq[0] == "e":
                exon = True
            else:
                if exon:
                    editseq = editseq + seq[0]
        seq = seq[1:]
    return editseq


def dnaToProtein(seq):
    return transcribe(translate(complement(seq)))


def compare(seq, mut):
    if seq == mut:
        return "None"
    seqP = dnaToProtein(seq)
    mutP = dnaToProtein(mut)
    if len(seq) == len(mut):
        mutation = "Substitution "
    else:
        mutation = "Insertion/Deletion "
    if seqP == mutP:
        return mutation + "(Silent)"
    else:
        if len(mutP) < len(seqP):
            return mutation + "(Nonsense)"
        else:
            return mutation + "(Missense)"


# Common DNA Manipulation Functions

def reverse(s):
    s = s[0:3] + s[len(s) - 4:2:-1] + s[len(s) - 3:len(s)]
    s = s.replace("5", "N")
    s = s.replace("3", "5")
    s = s.replace("N", "3")
    return s


def complement(s):
    s = s.replace("5", "N")
    s = s.replace("3", "5")
    s = s.replace("N", "3")
    s = s.replace("A", "N")
    s = s.replace("T", "A")
    s = s.replace("N", "T")
    s = s.replace("C", "N")
    s = s.replace("G", "C")
    s = s.replace("N", "G")
    return s


def translate(s):
    s = complement(s)
    s = s.replace("T", "U")
    return s


def deTranslate(s):
    s = s.replace("U", "T")
    s = complement(s)
    return s


STRAND_TYPE = ["sense", "template", "rna"]


def dnaReport(seq, strand):
    print "given", strand, seq, "\n"
    if strand not in STRAND_TYPE:
        print "Invalid strand type."
        print "Acceptable arguments: 'sense' 'template' 'rna'"
        return
    if strand == "template":
        seq = complement(seq)
    if strand == "rna":
        seq = complement(deTranslate(seq))
    if seq[0] == "3":
        print "reverse sense", seq
        seq = reverse(seq)
    seq = checkExonIntron(seq)
    print "sense", seq
    seq = complement(seq)
    print "template", seq
    seq = translate(seq)
    print "rna", seq
    seq = transcribe(seq)
    print "protein", seq
    return


def mutationReport(seq, mut):
    print "wild-type sequence", sequence
    print "mutated sequence", mutated
    print "wild-type protein", dnaToProtein(sequence)
    print "mutated protein", dnaToProtein(mutated)
    print "mutation", compare(sequence, mutated)


print "Problem 1: What is the amino acid sequence of the"
print "protein produced from translation of the following"
print "mRNA molecule?\n"

dnaReport("5'-AUGUCCCCUGUUUGA-3'", "rna")
print "\n\n"

print "Problem 2: What is the amino acid sequence of the"
print "protein produced from the following DNA sequence"
print "on the sense strand of the DNA molecule?\n"

dnaReport("5'-ATGAATCATTAGGGT-3'", "sense")
print "\n\n"

print "Problem 3: What is the amino acid sequence of the"
print "protein produced from the following DNA sequence"
print "on the template strand of the DNA molecule?\n"

dnaReport("3'-TACCTCCAGGTAACT-5'", "template")
print "\n\n"

print "Problem 4: What is the amino acid sequence of the"
print "protein produced from the following DNA sequence"
print "on the template strand of the DNA molecule?\n"

dnaReport("5'-GTATTATCTAGGCAT-3'", "template")
print "\n\n"

print "Problem 5: What is the amino acid sequence of the"
print "protein produced from the following DNA sequence"
print "on the sense strand of the DNA molecule, with exons"
print "and introns as indicated?\n"

dnaReport("e5'-ATGiACGATGeAAAACCiTTGACTAUGTCAeACATTA-3'", "sense")
print "\n\n"

print "Problem 6: Consider the DNA sequence on the sense strand"
print
sequence = "5'-ATGTGTCACAACGAGTAG-3'"
print sequence
print
print "that will express the following protein:"
print
print dnaToProtein(sequence)
print
print "The DNA sequences below each contain a mutation"
print "relative to the above sequence. Identify the type"
print "of mutation and the protein sequence that will be"
print "produced."
print
mutated = "5'-ATGTGACACAACGAGTAG-3'"
mutationReport(sequence, mutated)
print
mutated = "5'-ATGTGTCATAACGAGTAG-3'"
mutationReport(sequence, mutated)
print
mutated = "5'-ATGTGACAACGAGTAG-3'"
mutationReport(sequence, mutated)
