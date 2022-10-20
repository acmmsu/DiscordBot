"""
Unittest for encryption files.

By Anthony Eid
Date: 10/20/2022
"""

from unittest import TestCase
from encrypt import encrypt_basic, decrypt_basic


class test_encrypt(TestCase):
    
    def test_basic(self):
        
        # Set up test
        arg_str = "Geeks For Geeks"
        expected = "Gsree keFGsKoe"
        actual = encrypt_basic(arg_str)
        
        self.assertEqual(actual, expected)
    
    def test_decrypt(self):
        # Set up test
        arg_str = "Gsree keFGsKoe"
        expected = "Geeks For Geeks"
        actual = decrypt_basic(arg_str)
        
        self.assertEqual(actual, expected)
        
        