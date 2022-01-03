# find the complementry of dna
import sys
seq = sys.argv[1]
DNA = 'ACGT'
RNA = 'ACGU'



c = ''
for i in seq:
    if i == 'A':
        c += 'T'
    if i == 'T':
        c += 'A'
    if i == 'C':
        c += 'G'
    if i == 'G':
        c += 'C'    
print (c[::-1])

