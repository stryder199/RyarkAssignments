import string
from caesar_util import caesar_encrypt

def test_caesar_encrypt():
    lengths = [0, 1, 2, 3, 10]
    keys = [0, 1, 24, 25]
    plaintext_chars_list = ['ABYZ', 'CDEFGHIJKLMNOPQRSTUVWX']
    
    for length_index in range(len(lengths)):
        for keys_index in range(len(keys)):
            for plaintext_chars_index in range(len(plaintext_chars_list)):
                length = lengths[length_index]
                key = keys[keys_index]
                plaintext_chars = plaintext_chars_list[plaintext_chars_index]
                
                plaintext = ''
                expected_output = ''
                for i in range(length):
                    # Get the character we want to add to the test string
                    plaintext_char = plaintext_chars[i % len(plaintext_chars)]
                    
                    plaintext += plaintext_char
                    
                    # Get the index of the plaintext character in the alphabet
                    plaintext_char_index = string.uppercase.index(plaintext_char)
                    
                    # Get the index of the encrypted character in the alphabet
                    ciphertext_char_index = (plaintext_char_index + key) % len(string.uppercase)
                    
                    # Use that index and add the key to find the new index of the encrypted char
                    expected_output += string.uppercase[ciphertext_char_index]
                
                actual_output = caesar_encrypt(plaintext, key)
                
                if actual_output != expected_output:
                    print "plaintext: " + plaintext + ", key: " + str(key) + ", actual output: " + caesar_encrypt(plaintext, key) + ", expected output: " + expected_output
    
if __name__ == '__main__':
    test_caesar_encrypt()