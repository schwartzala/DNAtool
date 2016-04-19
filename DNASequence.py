STRAND_TYPE = ["sense", "template", "rna"]


class DNASequence():
    sequence = ""
    type = ""
    start = 0
    end = 0

    def __toString__(self):
        return self.start + "'-" + self.sequence + "-" + self.DNASequence.end + "'"

    def __reverse__(self):
        self.sequence = self.sequence[len(self.sequence)-1:0:-1]


def build_sequence(type, start, sequence):
    if type not in STRAND_TYPE:
        print "Invalid strand type."
        print "Acceptable arguments: 'sense' 'template' 'rna'"
        return
    seq = DNASequence()
    switcher = {
        "sense": sequence,
        "template": complement(sequence),
        "rna": complement(detranslate(seq))
    }
    seq.sequence = switcher.get(type)
    if start == 3:
        seq.sequence = reverse(seq.sequence)
    seq.start = 5
    seq.end = 3
    return seq


def reverse(s):
    return


def complement(s):
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


def detranslate(s):
    s = s.replace("U", "T")
    s = complement(s)
    return s
