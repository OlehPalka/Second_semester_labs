"""
Module with animals
"""


class Animal:
    """
    Animals class
    """

    def __init__(self, gender: bool, power: float):
        self.gender = gender
        self.power = power


class Bear(Animal):
    """
    Bear class
    """

    def __init__(self, gender, power):
        super().__init__(gender, power)
        self.letter = "B"


class Fish(Animal):
    """
    Fish class
    """

    def __init__(self, gender, power):
        super().__init__(gender, power)
        self.letter = "F"
