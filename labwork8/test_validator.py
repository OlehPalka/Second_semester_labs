""""
This is testing module.
"""
import unittest
from validator import Validator


class TestValidator(unittest.TestCase):
    """
    Class which tests function from module disc
    """

    def test_validator(self):
        """
        This method cheks if the functtion works correctly.
        """
        valid = Validator()
        self.assertEqual(valid.validate_name_surname("Elvis Presley"), True)
        self.assertEqual(valid.validate_name_surname("ElvisPresley"), False)
        self.assertEqual(valid.validate_name_surname(
            "Elvis Presley forever"), False)
        self.assertEqual(valid.validate_name_surname("elvis Presley"), False)
        self.assertEqual(valid.validate_name_surname("Elvis presley"), False)
        self.assertEqual(valid.validate_name_surname("Elvis PResley"), False)
        self.assertEqual(valid.validate_name_surname(
            "Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"), False)
        self.assertEqual(valid.validate_name_surname("Elvis P"), False)
        self.assertEqual(valid.validate_name_surname("Elvis P,resley"), False)
        self.assertEqual(valid.validate_name_surname("El1vis Presley"), False)
        self.assertEqual(valid.validate_age("20"), True)
        self.assertEqual(valid.validate_age("7"), False)
        self.assertEqual(valid.validate_age("100"), False)
        self.assertEqual(valid.validate_age("20."), False)
        self.assertEqual(valid.validate_age("20a"), False)
        self.assertEqual(valid.validate_age("12"), False)
        self.assertEqual(valid.validate_country("Ukraine"), True)
        self.assertEqual(valid.validate_country("U"), False)
        self.assertEqual(valid.validate_country(
            "UUUUUUUUUUUUUUUUUUUUUUU"), False)
        self.assertEqual(valid.validate_country("Ukraine1"), False)
        self.assertEqual(valid.validate_country("ukraine"), False)
        self.assertEqual(valid.validate_country("USA"), True)
        self.assertEqual(valid.validate_region("Lviv"), True)
        self.assertEqual(valid.validate_region("Lviv1"), True)
        self.assertEqual(valid.validate_region("L"), False)
        self.assertEqual(valid.validate_region("lviv"), False)
        self.assertEqual(valid.validate_living_place(
            "Koselnytska st. 2a"), True)
        self.assertEqual(valid.validate_living_place(
            "koselnytska st. 2a"), False)
        self.assertEqual(valid.validate_living_place(
            "Koselnytska provulok 2a"), False)
        self.assertEqual(valid.validate_living_place(
            "Koselnytska st. 2"), False)
        self.assertEqual(valid.validate_living_place(
            "Koselnytska st. a2"), False)
        self.assertEqual(valid.validate_living_place(
            "Koselnytska st. 22"), True)

    def test_phone_mail(self):
        """
        This method cheks if the functtion works correctly.
        """
        valid = Validator()
        self.assertEqual(valid.validate_index("79000"), True)
        self.assertEqual(valid.validate_index("7900"), False)
        self.assertEqual(valid.validate_index("790000"), False)
        self.assertEqual(valid.validate_index("7900q"), False)
        self.assertEqual(valid.validate_index("790 00"), False)
        self.assertEqual(valid.validate_phone("+380951234567"), True)
        self.assertEqual(valid.validate_phone("+38 (095) 123-45-67"), True)
        self.assertEqual(valid.validate_phone("38 (095) 123-45-67"), False)
        self.assertEqual(valid.validate_phone("380951234567"), False)
        self.assertEqual(valid.validate_phone("-380951234567"), False)
        self.assertEqual(valid.validate_phone("+3810951234567"), False)
        self.assertEqual(valid.validate_phone("+20951234567"), True)
        self.assertEqual(valid.validate_email("username@domain.com"), True)
        self.assertEqual(valid.validate_email(
            "username+usersurname@domain.com"), True)
        self.assertEqual(valid.validate_email("username@ucu.edu.ua"), True)
        self.assertEqual(valid.validate_email("usernamedomain.com"), False)
        self.assertEqual(valid.validate_email("usernam..edomain.com"), False)
        self.assertEqual(valid.validate_email("username@domaincom"), False)
        self.assertEqual(valid.validate_email("username@domain.aaa"), False)
        self.assertEqual(valid.validate_email("username@aaa"), False)
        self.assertEqual(valid.validate_email("@domain.com"), False)
        self.assertEqual(valid.validate_id("123450"), True)
        self.assertEqual(valid.validate_id("011111"), True)
        self.assertEqual(valid.validate_id("123456"), False)
        self.assertEqual(valid.validate_id("123006"), False)
        self.assertEqual(valid.validate_id("1230916"), False)
        self.assertEqual(valid.validate_id("12306"), False)
        self.assertEqual(valid.validate(
            "Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,\
+380951234567,username@domain.com,123450"), True)
        self.assertEqual(valid.validate(
            "Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;\
+380951234567;username@domain.com;123450"), True)
        self.assertEqual(valid.validate(
            "Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000;\
 +380951234567; username@domain.com; 123450"), True)
        self.assertEqual(valid.validate(
            "Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000,\
 +380951234567, username@domain.com, 123450"), True)
        self.assertEqual(valid.validate(
            "ElvisPresley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, \
+380951234567, username@domain.com, 123450"), False)


if __name__ == "__main__":
    unittest.main()
