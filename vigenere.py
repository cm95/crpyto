#author Christopher Millar 

import string 

numberL = []
numberK = []
en = []
complete=[]
#ciphertext to be deencrypted 
cWord = list("NQWFCRHYIRZKIIJOZLHFWKVAWGMXMM") 
#key of ciphertext
key = list("TESSOFTHEDURBERVILLES")

#give numerical value to each letter (0-25) put in numberL list 
for i in cWord:
	le = string.uppercase.index(i)
	numberL.append(le)
	
#give numerical value to each letter (0-25) put in numberK list 
for i in key:
	ke = string.uppercase.index(i)
	numberK.append(ke)
	
print numberL
print numberK	

j=0
for i in numberL:
	x = i - numberK[j]
	x = x%26
	en.append(x)
	j = j+1 # next element in list 
	j = j%len(key) # loops around key list 

for i in en:
	le = string.uppercase[i]
	complete.append(le)
		
		
print (''.join(complete))
print "\n"