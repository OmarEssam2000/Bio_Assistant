# counting dna nucleotides
import sys
seq = sys.argv[1]
DNA = 'ACGT'
RNA = 'ACGU'


def countingnuc(seq):
    ns = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in seq:
        ns[n] += 1
    return ns


print(countingnuc(seq))
