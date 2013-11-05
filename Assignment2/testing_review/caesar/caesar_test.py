import unittest

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

class TestCaesarEncrypt(unittest.TestCase):
    
    def test_caesar_encrypt(self):
        lengths = [0, 1, 2, 3, 10]
        keys = [0, 1, 24, 25]
        plaintext_chars_list = ['ABYZ', 'CDEFGHIJKLMNOPQRSTUVWX']
        
        test_count = 0
        for length_index in range(len(lengths)):
            for keys_index in range(len(keys)):
                for plaintext_chars_index in range(len(plaintext_chars_list)):
                    length = lengths[length_index]
                    key = keys[keys_index]
                    plaintext_chars = plaintext_chars_list[plaintext_chars_index]
                    
                    plaintext = ''
                    for i in range(length):
                        plaintext += plaintext_chars[i % len(plaintext_chars)]
                        
                    print str(test_count) + ": " + plaintext
#         self.assertEqual(caeser_encrypt('HI', 0), 'HI', "Caesar Encrypt #1")
#         self.assertEqual(caeser_encrypt('HI', 26), 'HI', "Caesar Encrypt #2")
#         self.assertEqual(caeser_encrypt('HI', 1), 'IJ', "Caesar Encrypt #3")
    
if __name__ == '__main__':
    unittest.main()