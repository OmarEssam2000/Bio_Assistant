#converting dna to rna
import sys
seq2=sys.argv[1]
DNA='ACGT'
RNA='ACGU'

seq2.replace('T','U')
print(seq2)