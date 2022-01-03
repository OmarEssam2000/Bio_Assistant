# check the validation of dna seqences
import sys
seq= sys.argv[1]
DNA='ACGT'
RNA='ACGU'

def DNAValidation(dnaseq):
    for n in dnaseq:
        if n not in DNA:
            return False
    return True

print(DNAValidation(seq))

