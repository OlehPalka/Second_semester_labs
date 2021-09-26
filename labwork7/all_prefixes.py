"""
This module has two functions which make operations wwith words.
"""


def add_char(set_pref, list_of_letters):
    """
    This function adds cmbinations of letters to the set.
    """
    added_char = ""
    for i in enumerate(list_of_letters):
        added_char += list_of_letters[i[0]]
        set_pref.add(added_char)
    return set_pref


def all_prefixes(word):
    """
    This function completes whole process of adding frases.
    """
    set_of_pref = set()
    word = list(word)
    first_letter = word[0]
    while word != []:
        add_char(set_of_pref, word)
        word_len = len(word)
        for _ in range(word_len):
            del word[0]
            try:
                if word[0] == first_letter:
                    break
            except IndexError:
                break
    return set_of_pref
