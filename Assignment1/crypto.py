#TODO Test Cases
#TODO Clean up some algorithms

'''
purpose
	encrypt P using Caesar cipher with key K
preconditions
	P: string of A..Z
	K in 0..25
'''
def caeser_encrypt(P,K):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	cipherString = ""
	for p in P:
		index_c = alpha.index(p) + K
		index_c = index_c % 26
		cipherString += alpha[index_c]
	return cipherString

'''
purpose
	decrypt C using Caesar cipher with key K
preconditions
	C: string of A..Z
	K in 0..25
'''
def caeser_decrypt(C,K):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	plainString = ""
	for c in C:
		index_p = alpha.index(c) - K
		index_p = index_p % 26
		plainString += alpha[index_p]
	return plainString

# --------------------------------------------------------------

'''
purpose
	encrypt P using substitution cipher with key K
preconditions
	P: string of A..Z
	K: permutation of A..Z
'''
def substitution_encrypt(P,K):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	cipherString = ""
	for p in P:
		index_c = alpha.index(p)
		cipherString += K[index_c]
	return cipherString


'''
purpose
	decrypt C using substitution cipher with key K
preconditions
	C: string of A..Z
	K: permutation of A..Z
'''
def substitution_decrypt(C,K):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	plainString = ""
	for c in C:
		index_p = K.index(c)
		plainString += alpha[index_p]
	return plainString


# --------------------------------------------------------------

'''
purpose
	encrypt P using Vernam cipher with key K
	if len(P) > len(K) then repeat the key as needed
preconditions
	P: string of A..Z
	K: non-empty list of int in 0..25
'''
def vernam_encrypt(P,K):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	key_index = 0
	cipherString = ""
	
	for p in P:
		c_index = alpha.index(p) + K[key_index]
		c_index = c_index % 26
		cipherString += alpha[c_index]
		if key_index+1 == len(K):
			key_index = 0
		else:
			key_index += 1
	return cipherString


'''
purpose
	decrypt C using Vernam cipher with key K
	if len(C) > len(K) then repeat the key as needed
preconditions
	C: string of A..Z
	K: non-empty list of int in 0..25
'''
def vernam_decrypt(C,N):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	key_index = 0
	plainString = ""
	
	for c in C:
		p_index = alpha.index(c) - N[key_index]
		p_index = p_index % 26
		plainString += alpha[p_index]
		if key_index+1 == len(N):
			key_index = 0
		else:
			key_index += 1
	return plainString


# --------------------------------------------------------------

'''
purpose
	encrypt P using book cipher with key K
	if len(P) > len(K) then repeat the key as needed
preconditions
	P: string of A..Z
	K: non-empty string of A..Z
'''
def book_encrypt(P,K):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	key_index = 0
	cipherString = ""
	
	for p in P:
		c_index = alpha.index(p) + alpha.index(K[key_index])
		c_index = c_index % 26
		cipherString += alpha[c_index]
		if key_index+1 == len(K):
			key_index = 0
		else:
			key_index += 1
			
	return cipherString


'''
purpose
	decrypt C using book cipher with key K
	if len(C) > len(K) then repeat the key as needed
preconditions
	C: string of A..Z
	K: non-empty string of A..Z
'''
def book_decrypt(C,N):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	key_index = 0
	plainString = ""
	
	for c in C:
		p_index = alpha.index(c) - alpha.index(N[key_index])
		p_index = p_index % 26
		plainString += alpha[p_index]
		if key_index+1 == len(N):
			key_index = 0
		else:
			key_index += 1
			
	return plainString


# --------------------------------------------------------------

'''
purpose
	encrypt P using columnar transposition cipher with key K
preconditions
	P: string of A..Z
	K > 1
'''
def columnar_encrypt(P,K):
	cipherString = ""
	
	if K >= len(P) or K == 1:
		return P
	
	for i in range(K):
		for j in range(len(P)/K):
			cipherString += P[i + j*K]
			
			if j == len(P)/K-1 and i < len(P)%K:
				cipherString += P[i + (j+1)*K]
	return cipherString			
	
'''
purpose
	decrypt C using columnar transposition cipher with key K
preconditions
	P: string of A..Z
	K > 1
'''
def columnar_decrypt(C,K):
	plainString = ""

	jumps = len(C)/K
	if len(C)%K > 0:
		jumps += 1
		
	for i in range(jumps):
		jump_index = i
		number_of_jumps = K
		if i == jumps-1 and len(C)%K > 0:
			number_of_jumps = len(C)%K
		for j in range(number_of_jumps):
			plainString += C[jump_index]
			jump_index += len(C)/K
			if j < len(C)%K:
				jump_index += 1
	return plainString

# --------------------------------------------------------------

'''
purpose
	encrypt P using RSA encryption with key K e,n
preconditions
	P: list of positive integers
	e,n selected according to the RSA requirements
'''
def rsa_encrypt(P,e,n):
	cipherList = []
	for p in P:
		c = (p**e)%n
		cipherList.append(c)
		
	return cipherList

'''
purpose
	decrypt C using RSA encryption with key K d,n
preconditions
	C: list of positive integers
	d,n selected according to the RSA requirements
'''
def rsa_decrypt(C,d,N):
	plainList = []
	for c in C:
		p = (c**d)%N
		plainList.append(p)
	
	return plainList

# --------------------------------------------------------------

'''
purpose
	return a list L where
		len(L) = 26
		L[i] contains the number of occurrences in S of the ith
			letter in the alphabet
preconditions
	S is a string of A..Z
'''
def count_letters(S):
	counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in S:
		counts[alpha.index(letter)] += 1
	return counts


# --------------------------------------------------------------

'''
purpose
	return a dictionary D where
		D.keys contains all of the digrams in S
		D[d] is the number of occurrences of digram d in S
preconditions
	S is a string of A..Z
'''
def count_digrams(S):
	counts = {}
	for s_index in range(len(S)-1):
		digram = S[s_index] + S[s_index+1]
		if not counts.has_key(digram):
			counts[digram] = 1
		else:
			counts[digram] += 1
	return counts