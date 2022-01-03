#counting pointing mutations
import sys
s1= sys.argv[1]
s2= sys.argv[2]

def countmutations(s1,s2):
    m=0
    for i in range(0,len(s1)):
        if s1[i]==s2[i]:
            continue
        else:
            m+=1
    return m
print(countmutations(s1, s2))