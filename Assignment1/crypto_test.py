import unittest
from crypto import *

class TestCryptoFunctions(unittest.TestCase):
    
    def test_caesar_encrypt(self):
        print "Starting Caesar Encrypt"
        self.assertEqual(caeser_encrypt('HI', 0), 'HI', "Caesar Encrypt #1")
        self.assertEqual(caeser_encrypt('HI', 26), 'HI', "Caesar Encrypt #2")
        self.assertEqual(caeser_encrypt('HI', 1), 'IJ', "Caesar Encrypt #3")
        print "Finished Caesar Encrypt\n"
        
    def test_caesar_decrypt(self):
        print "Starting Caesar Decrypt"
        self.assertEqual(caeser_decrypt('HI', 0), 'HI', "Caesar Decrypt #1")
        self.assertEqual(caeser_decrypt('HI', 26), 'HI', "Caesar Decrypt #2")
        self.assertEqual(caeser_decrypt('HI', 1), 'GH', "Caesar Decrypt #3")
        print "Finished Caesar Decrypt\n"
        
    def test_substitution_encrypt(self):
        print "Starting Substitution Encrypt"
        print "Finished Substitution Encrypt\n"
    
    def test_substitution_decrypt(self):
        print "Starting Substitution Decrypt"
        print "Finished Substitution Decrypt\n"
    
    def test_vernam_encrypt(self):
        print "Starting Vernam Encrypt"
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER', "Vernam Encrypt #1")
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48, 88]), 'TAHRSPITXMAB', "Vernam Encrypt #2")
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER', "Vernam Encrypt #3")
        self.assertEqual(vernam_encrypt('VERNAMCIPHER', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48]), 'TAHRSPITXMAP', "Vernam Encrypt #4")
        print "Finished Vernam Encrypt\n"
        
    def test_vernam_decrypt(self):
        print "Starting Vernam Decrypt"
        self.assertEqual(vernam_decrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER', "Vernam Decrypt #1")
        self.assertEqual(vernam_decrypt('TAHRSPITXMAB', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48, 88]), 'VERNAMCIPHER', "Vernam Decrypt #2")
        self.assertEqual(vernam_decrypt('VERNAMCIPHER', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'VERNAMCIPHER', "Vernam Decrypt #3")
        self.assertEqual(vernam_decrypt('TAHRSPITXMAP', [76, 48, 16, 82, 44, 03, 58, 11, 60, 05, 48]), 'VERNAMCIPHER', "Vernam Decrypt #4")
        print "Finished Vernam Decrypt\n"
        
    def test_book_encrypt(self):
        print "Starting Book Encrypt"
        print "Finished Book Encrypt\n"
    
    def test_book_decrypt(self):
        print "Starting Book Decrypt"
        print "Finished Book Decrypt\n"
    
    def test_columnar_encrypt(self):
        print "Starting Columnar Encrypt"
        #One line down
        self.assertEqual(columnar_encrypt('ILOVETOENCRYPTTHINGS', 2), 'IOEONRPTIGLVTECYTHNS', "Columnar Encrypt #1")
        
        #One solid block of text, no mods
        self.assertEqual(columnar_encrypt('ILOVETOENCRYPTTHINGS', 5), 'ITRHLOYIOEPNVNTGECTS', "Columnar Encrypt #2")
        
        #One mod letter
        self.assertEqual(columnar_encrypt('IREALLYLOVETOENCRYPTTHINGS', 5), 'ILECTSRYTRHELOYIAOEPNLVNTG', "Columnar Encrypt #3")
        
        #One full mod row with one missing
        self.assertEqual(columnar_encrypt('ILOVETOENCRYPTTHINGS', 7), 'IETLNHOCIVRNEYGTPSOT', "Columnar Encrypt #4")
        
        #K equals to the length
        self.assertEqual(columnar_encrypt('ILOVETOENCRYPTTHINGS', 20), 'ILOVETOENCRYPTTHINGS', "Columnar Encrypt #5")
        
        #K greater than the length
        self.assertEqual(columnar_encrypt('ILOVETOENCRYPTTHINGS', 21), 'ILOVETOENCRYPTTHINGS', "Columnar Encrypt #6")
        print "Finished Columnar Encrypt\n"
    
    def test_columnar_decrypt(self):
        print "Starting Columnar Decrypt"
        #One line down
        self.assertEqual(columnar_decrypt('IOEONRPTIGLVTECYTHNS', 2), 'ILOVETOENCRYPTTHINGS', "Columnar Decrypt #1")
        
        #One solid block of text, no mods
        self.assertEqual(columnar_decrypt('ITRHLOYIOEPNVNTGECTS', 5), 'ILOVETOENCRYPTTHINGS', "Columnar Decrypt #2")

        #One mod letter
        self.assertEqual(columnar_decrypt('ILECTSRYTRHELOYIAOEPNLVNTG', 5), 'IREALLYLOVETOENCRYPTTHINGS', "Columnar Decrypt #3")
        
        #One full mod row with one missing
        self.assertEqual(columnar_decrypt('IETLNHOCIVRNEYGTPSOT', 7), 'ILOVETOENCRYPTTHINGS', "Columnar Decrypt #4")
        
        #K equal to the length
        self.assertEqual(columnar_decrypt('ILOVETOENCRYPTTHINGS', 20), 'ILOVETOENCRYPTTHINGS', "Columnar Decrypt #5")
        
        #K one greater than the length
        self.assertEqual(columnar_decrypt('ILOVETOENCRYPTTHINGS', 21), 'ILOVETOENCRYPTTHINGS', "Columnar Decrypt #6")
        print "Finished Columnar Decrypt\n"
    
    def test_rsa_encrypt(self):
        print "Starting RSA Encrypt"
        self.assertEqual(rsa_encrypt([2, 3, 20, 11, 13, 15, 16, 19, 10, 14], 17, 470929), [131072, 105617, 266988L, 227340L, 393425L, 37661L, 157007L, 1140L, 347522L, 146068L], "RSA Encrypt #1")
        self.assertEqual(rsa_encrypt([13, 8, 4, 10, 11, 22, 25, 2, 15, 9], 17, 470929), [393425L, 96697L, 379264L, 347522L, 227340L, 346934L, 336312L, 131072, 37661L, 55466L], "RSA Encrypt #2")
        self.assertEqual(rsa_encrypt([3, 24, 2, 23, 9, 12, 10, 0, 13, 19], 17, 470929), [105617, 280755L, 131072, 429540L, 55466L, 447006L, 347522L, 0, 393425L, 1140L], "RSA Encrypt #3")
        self.assertEqual(rsa_encrypt([8, 25, 23, 0, 13, 4, 11, 19, 18, 20], 17, 470929), [96697L, 336312L, 429540L, 0, 393425L, 379264L, 227340L, 1140L, 308579L, 266988L], "RSA Encrypt #4")
        self.assertEqual(rsa_encrypt([0, 4, 8, 14, 23, 19, 5, 2, 16, 7], 17, 470929), [0, 379264L, 96697L, 146068L, 429540L, 1140L, 95308L, 131072, 157007L, 191934L], "RSA Encrypt #5")
        print "Finished RSA Encrypt\n"
    
    def test_rsa_decrypt(self):
        print "Starting RSA Decrypt"
        self.assertEqual(rsa_decrypt([131072, 105617, 266988L, 227340L, 393425L, 37661L, 157007L, 1140L, 347522L, 146068L], 110465, 470929), [2, 3, 20, 11, 13, 15, 16, 19, 10, 14], "RSA Decrypt #1")
        self.assertEqual(rsa_decrypt([393425L, 96697L, 379264L, 347522L, 227340L, 346934L, 336312L, 131072, 37661L, 55466L], 110465, 470929), [13, 8, 4, 10, 11, 22, 25, 2, 15, 9], "RSA Decrypt #2")
        self.assertEqual(rsa_decrypt([105617, 280755L, 131072, 429540L, 55466L, 447006L, 347522L, 0, 393425L, 1140L], 110465, 470929), [3, 24, 2, 23, 9, 12, 10, 0, 13, 19], "RSA Decrypt #3")
        self.assertEqual(rsa_decrypt([96697L, 336312L, 429540L, 0, 393425L, 379264L, 227340L, 1140L, 308579L, 266988L], 110465, 470929), [8, 25, 23, 0, 13, 4, 11, 19, 18, 20], "RSA Decrypt #4")
        self.assertEqual(rsa_decrypt([0, 379264L, 96697L, 146068L, 429540L, 1140L, 95308L, 131072, 157007L, 191934L], 110465, 470929), [0, 4, 8, 14, 23, 19, 5, 2, 16, 7], "RSA Decrypt #5")
        print "Finished RSA Decrypt\n"
    
    def test_count_letters(self):
        pass
    
    def test_count_digrams(self):
        pass
    
if __name__ == '__main__':
    unittest.main()