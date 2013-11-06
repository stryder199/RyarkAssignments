# intentionally empty; no util functions needed

'''
purpose
    encrypt P using Caesar cipher with key K
preconditions
    P: string of A..Z
    K in 0..25
'''
def caesar_encrypt(P,K):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipherString = ""
    P = P.upper()
    
    for p in P:
        index_c = alpha.index(p) + K
        index_c = index_c % 26
        cipherString += alpha[index_c] #DR4
    cipherString = cipherString.lower()
            
    return cipherString