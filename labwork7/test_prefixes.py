"""
Testing module for prefixes.
"""

from all_prefixes import *
import unittest


class Prefixes(unittest.TestCase):
    """
    Class which tests function from module prefixes
    """

    def test_pref(self):
        """
        This method cheks if the functtion works correctly.
        """
        self.assertEqual({"l", "le", "lea", "lead"}, all_prefixes("lead"))
        self.assertEqual({"л", "ло", "лоб"}, all_prefixes("лоб"))
        self.assertEqual({"с", "со", "соу", "соус", "соуси",
                          "си"}, all_prefixes("соуси"))

    def test_pref_1(self):
        """
        This method cheks if the functtion works correctly.
        """
        self.assertEqual({'анг', 'аа', 'аанг', 'а', 'аан',
                          'ан'}, all_prefixes("аанг"))

    def test_pref_2(self):
        """
        This method cheks if the functtion works correctly.
        """
        self.assertEqual({'п', 'пром', 'про', 'пр'}, all_prefixes("пром"))

    def test_pref_3(self):
        """
        This method cheks if the functtion works correctly.
        """
        self.assertEqual({'п', 'помпа', 'помп', 'по', 'па',
                          'пом'}, all_prefixes("помпа"))

    def test_pref_3(self):
        """
        This method cheks if the functtion works correctly.
        """
        self.assertEqual({'п', 'помпа', 'помп', 'по',
                          'пом'}, add_char(set(), ["п", "о", "м", "п", "а"]))


if __name__ == "__main__":
    unittest.main()
