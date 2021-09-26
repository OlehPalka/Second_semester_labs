"""
This module contains testing class for cipher.
"""

import unittest
from vigenere_cipher import *


class TestCipher(unittest.TestCase):
    """
    Class which tests function from module task_1
    """

    def test_encode_character(self):
        """
        
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        self.assertEqual(encoded, "X")

    def test_encode_spaces(self):
        """
        
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_lowercase(self):
        """
        
        """
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_decode(self):
        """
        
        """
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        self.assertEqual(decoded, "ENCODEDINPYTHON")

    def test_separate_character(self):
        """
        
        """
        self.assertEqual(separate_character("X", "T"), "E")
        self.assertEqual(separate_character("E", "R"), "N")


unittest.main()
