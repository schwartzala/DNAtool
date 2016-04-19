def file_to_dna(file):
    sequence = ""
    with open(file) as f:
        for line in f:
            line = line.replace('\n', '')
            sequence = sequence + line
    if "U" in sequence:
        strand_type = "RNA"
    else:
        strand_type = "DNA"
    return [sequence, strand_type]


def rna_to_dna(sequence):
    sequence = sequence.replace("A", "T")
    sequence = sequence.replace("U", "A")
    sequence = sequence.replace("C", " ")
    sequence = sequence.replace("G", "C")
    sequence = sequence.replace(" ", "G")
    return sequence


def read_dna(sequence):
    return sequence


dna_file_path = "dna.txt"
dna = file_to_dna(dna_file_path)
print dna[0]
print dna[1]
if dna[1] == "RNA":
    dna[0] = rna_to_dna(dna[0])
    dna[1] = "DNA"
print dna[0]
print dna[1]

rna_file_path = "rna.txt"
rna = file_to_dna(rna_file_path)
print rna[0]
print rna[1]
if rna[1] == "RNA":
    rna[0] = rna_to_dna(rna[0])
    rna[1] = "DNA"
print rna[0]
print rna[1]
