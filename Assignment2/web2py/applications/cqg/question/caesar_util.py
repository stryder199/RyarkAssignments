# intentionally empty; no util functions needed

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