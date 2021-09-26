"""
This is module for validating user data
"""
import re


class Validator:
    """
    Class which creates validator.
    """

    def validate_name_surname(self, name_surname: str):
        """
        Check if the name and surname are correct.
        """
        return bool(re.fullmatch("[A-Z][a-z]{1,29} [A-Z][a-z]{1,29}", name_surname))

    def validate_age(self, age: str):
        """
        Checks if the age is correct.
        """
        return bool(re.fullmatch("1[6-9]|[2-9][0-9]", age))

    def validate_country(self, country: str):
        """
        Checks if the country is entered correctly.
        """
        return bool(re.fullmatch("[A-Z][A-Za-z]{1,9}", country))

    def validate_region(self, region: str):
        """
        Checks if the region is entered correctly.
        """
        return bool(re.fullmatch("[A-Z][A-Za-z0-9]{1,9}", region))

    def validate_living_place(self, living_place: str):
        """
        Checks if the place of living is entered correctly.
        """
        return bool(re.fullmatch("[A-Z][a-z]{2,19} \
(st.|av.|prosp.|rd.) [0-9][0-9a-z]", living_place))

    def validate_index(self, index: str):
        """
        Checks if the index is entered correctly.
        """
        return bool(re.fullmatch("[0-9]{5}", index))

    def validate_phone(self, phone: str):
        """
        Checks if the phone is entered correctly.
        """
        return bool(re.fullmatch("([+][0-9]{0,2} [(][0-9]{3}[)] [0-9]{3}[-]\
[0-9]{2}[-][0-9]{2})|([+][0-9]{9,12})", phone))

    def validate_email(self, email: str):
        """
        Checks if the email is entered correctly.
        """
        if len(re.findall("[.]{2}", email)) >= 1:
            return False
        return bool(re.fullmatch(r"""[^\.][A-Za-z0-9\!#$%&'*+-/\=?^_`{|}~]"""
                                 r"""{0,63}[@][a-z\.]{1,255}"""
                                 r"""[(?<=\.)(com|org|edu|gov|net|ua)][\.]"""
                                 r"""(com|org|edu|gov|net|ua)""", email))

    def validate_id(self, user_id: str):
        """
        Checks if the id is entered correctly.
        """
        if len(re.findall("[0]", user_id)) != 1:
            return False
        return bool(re.fullmatch("[0-9]{6}", user_id))

    def validate(self, data: str):
        """
        Checks if all the methods works correctly.
        """
        data = re.split(r", |; |,|;", data)
        if self.validate_name_surname(data[0]) and self.validate_age(data[1])\
                and self.validate_country(data[2]) and self.validate_region(data[3])\
                and self.validate_living_place(data[4]) and self.validate_phone(data[6]) \
                and self.validate_email(data[7]) and self.validate_id(data[8])\
                and self.validate_index(data[5]):
            return True
        return False


if __name__ == '__main__':
    valid = Validator()
    # name and surname
    assert valid.validate_name_surname("Elvis Presley") is True
    # Not 2 words
    assert valid.validate_name_surname("ElvisPresley") is False
    assert valid.validate_name_surname("Elvis Presley forever") is False

    # should be only first uppercase letter in name and surname
    assert valid.validate_name_surname("elvis Presley") is False
    assert valid.validate_name_surname("Elvis presley") is False
    assert valid.validate_name_surname("Elvis PResley") is False

    # size of both name and surname shoulb be between 2 and 30

    assert valid.validate_name_surname(
        "Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") is False
    assert valid.validate_name_surname("Elvis P") is False

    # no digits or punctuation in name or surname
    assert valid.validate_name_surname("Elvis P,resley") is False
    assert valid.validate_name_surname("El1vis Presley") is False

    # valid age id digit berween 16 and 99
    assert valid.validate_age("20") is True
    assert valid.validate_age("7") is False
    assert valid.validate_age("100") is False
    assert valid.validate_age("20.") is False
    assert valid.validate_age("20a") is False
    assert valid.validate_age("12") is False

    # valid country - between 2 and 10 chars,
    # first letter should be uppercase, can`t contain numbers
    assert valid.validate_country("Ukraine") is True
    assert valid.validate_country("U") is False
    assert valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU") is False
    assert valid.validate_country("Ukraine1") is False
    assert valid.validate_country("ukraine") is False
    assert valid.validate_country("USA") is True

    # valid region - the same as country, but can contain numbers
    assert valid.validate_region("Lviv") is True
    assert valid.validate_region("Lviv1") is True
    assert valid.validate_region("L") is False
    assert valid.validate_region("lviv") is False

    # living place - should be in format: "Koselnytska st. 2a"
    # name of street - between 3 and 20 chars, first character
    # uppercase, no digits in it
    # type of street - should be "st.", "av.", "prosp." or "rd."
    # number of building - exactly 2 symbols, first should be number,
    #  second can be number or small letter
    assert valid.validate_living_place("Koselnytska st. 2a") is True
    assert valid.validate_living_place("koselnytska st. 2a") is False
    assert valid.validate_living_place("Koselnytska provulok 2a") is False
    assert valid.validate_living_place("Koselnytska st. 2") is False
    assert valid.validate_living_place("Koselnytska st. a2") is False
    assert valid.validate_living_place("Koselnytska st. 22") is True

    # valid index - exactly 5 digits
    assert valid.validate_index("79000") is True
    assert valid.validate_index("7900") is False
    assert valid.validate_index("790000") is False
    assert valid.validate_index("7900q") is False
    assert valid.validate_index("790 00") is False

    # valid phone - in format "+380951234567" or "+38 (095) 123-45-67"
    # starts wit "+" and has from 9 to 12 numbers
    assert valid.validate_phone("+380951234567") is True
    assert valid.validate_phone("+38 (095) 123-45-67") is True
    assert valid.validate_phone("38 (095) 123-45-67") is False
    assert valid.validate_phone("380951234567") is False
    assert valid.validate_phone("-380951234567") is False
    assert valid.validate_phone("+3810951234567") is False
    assert valid.validate_phone("+20951234567") is True

    # valid email should be in format "username@domain.type"
    # username - any letters, digits, any of "!#$%&'*+-/=?^_`{|}~",
    #  dots (provided that it is not the first or last
    # character and provided also that it does not appear
    #  consecutively), at least 1, at most 64
    # domain - only lowercase letters, at least 1, at most 255, but
    # be careful - can be also "." - for example @ucu.edu.ua
    # type : "com", "org", "edu", "gov", "net", "ua",....
    assert valid.validate_email("username@domain.com") is True
    assert valid.validate_email("username+usersurname@domain.com") is True
    assert valid.validate_email("username@ucu.edu.ua") is True
    assert valid.validate_email("usernamedomain.com") is False
    assert valid.validate_email("username@domaincom") is False
    assert valid.validate_email("username@domain.aaa") is False
    assert valid.validate_email("username@aaa") is False
    assert valid.validate_email("@domain.com") is False

    # valid id - exactly 6 digits, but should contain
    # exactly one zero - at any position
    assert valid.validate_id("123450") is True
    assert valid.validate_id("011111") is True
    assert valid.validate_id("123456") is False
    assert valid.validate_id("123006") is False
    assert valid.validate_id("1230916") is False
    assert valid.validate_id("12306") is False

    # data - string in format "name_surname,age,country,
    # region,living_place,index,phone,email,id"
    # can also be whitespaces between sections and allowed separator ші ";"
    # all previous criteria are valid
    assert valid.validate(
        "Elvis Presley,20,Ukraine,Lviv,Koselnytska st. \
2a,79000,+380951234567,username@domain.com,123450") is True
    assert valid.validate(
        "Elvis Presley;20;Ukraine;Lviv;Koselnytska st. \
2a;79000;+380951234567;username@domain.com;123450") is True
    assert valid.validate(
        "Elvis Presley; 20; Ukraine; Lviv; Koselnytska\
 st. 2a; 79000; +380951234567; username@domain.com; 123450") is True
    assert valid.validate(
        "Elvis Presley, 20, Ukraine, Lviv, Koselnytska st.\
 2a, 79000, +380951234567, username@domain.com, 123450") is True
