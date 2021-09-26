"""
This module contains cipher class and funtions.
"""


class VigenereCipher:
    """
    This class creates object of cipher.
    """

    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        """
        THis method encodes text.
        """
        cipher = []
        plaintext = plaintext.replace(" ", "").upper()
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):
            cipher.append(combine_character(p, k))
        return "".join(cipher)

    def extend_keyword(self, number):
        """
        Extends keyword to the lenth of the plain text.
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def decode(self, ciphertext):
        """
        This method decodes encoded text.
        """
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append(separate_character(p, k))
        return "".join(plain)


def separate_character(cypher, keyword):
    """
    This function decodes a character 
    """
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)


def combine_character(plain, keyword):
    """
    This function encodes a character.
    """
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)
