# counting dna nucleotides
import sys
seq = sys.argv[3]
DNA = 'ACGT'
RNA = 'ACGU'



ns = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for n in seq:
    ns[n] += 1
    
A = str(ns['A']) 
C = str(ns['C'])
G = str(ns['G'])
T = str(ns['T'])
print ( 'A :' + A , 'C :' + C , 'G :' + G ,'T :' + T )



