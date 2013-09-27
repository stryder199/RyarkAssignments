'''
Created on Sep 26, 2013

@author: Ryan
'''

import unittest
from crypto import *

class TestCryptoFunctions(unittest.TestCase):
    
    def test_caesar_encrypt(self):
        self.assertEqual(caeser_encrypt('HI', 0), 'HI')
        self.assertEqual(caeser_encrypt('HI', 26), 'HI')
        
        self.assertEqual(caeser_encrypt('HI', 1), 'IJ')
        
    def test_caesar_decrypt(self):
        self.assertEqual(caeser_decrypt('HI', 0), 'HI')
        self.assertEqual(caeser_decrypt('HI', 26), 'HI')
        
        self.assertEqual(caeser_decrypt('HI', 1), 'GH')
        
    def test_substitution_encrypt(self):
        pass
    
    def test_substitution_decrypt(self):
        pass
    
    def test_vernam_encrypt(self):
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER')
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48, 88]), 'TAHRSPITXMAB')
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER')
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48]), 'TAHRSPITXMAP')
        
        
    def test_vernam_decrypt(self):
        self.assertEqual(vernam_decrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER')
        self.assertEqual(vernam_decrypt('TAHRSPITXMAB', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48, 88]), 'VERNAMCIPHER')
        self.assertEqual(vernam_decrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER')
        self.assertEqual(vernam_decrypt('TAHRSPITXMAP', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48]), 'VERNAMCIPHER')
        
    def test_book_encrypt(self):
        pass
    
    def test_book_decrypt(self):
        pass
    
    def test_columnar_encrypt(self):
        pass
    
    def test_columnar_decrypt(self):
        pass
    
    def test_rsa_encrypt(self):
        pass
    
    def test_rsa_decrypt(self):
        pass
    
    def test_count_letters(self):
        pass
    
    def test_count_digrams(self):
        pass
    
if __name__ == '__main__':
    unittest.main()