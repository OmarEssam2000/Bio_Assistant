#def naive(pattern,text):
#   pattern=pattern.capitalize()
#   text=text.capitalize()
#   occurance=[]
#   for i in range(len(text)-len(pattern)+1):
#         match=True
#         for j in range(len(pattern)):
#               if text[i+j] != pattern[j]:
#                      match=False
#                      break
#         if match:
#                occurance.append(i)
#   print(occurance)


#txt=input("enter the text ")
#pat=input("enter the pattern ")
#result=naive(pat,txt)
#print(result)
# Python3 program for Naive Pattern
# Searching algorithm
def search(pat, txt):
	M = len(pat)
	N = len(txt)

	# A loop to slide pat[] one by one */
	for i in range(N - M + 1):
		j = 0
		
		# For current index i, check
		# for pattern match */
		while(j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1

		if (j == M):
			print("Pattern found at index ", i)

# Driver Code

txt = input('enter text')
pat = input('enter pattern')
search(pat, txt)

# This code is contributed
# by PrinciRaj1992
