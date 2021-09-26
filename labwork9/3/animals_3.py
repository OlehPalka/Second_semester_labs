"""
Module with animals
"""


class Animal:
    """
    Animals class
    """

    def __init__(self, gender: bool, power: float, age: int):
        self.age = age
        self.gender = gender
        self.power = power


class Bear(Animal):
    """
    Bear class
    """

    def __init__(self, gender, power, age):
        super().__init__(gender, power, age)
        self.letter = "B"


class Fish(Animal):
    """
    Fish class
    """

    def __init__(self, gender, power, age):
        super().__init__(gender, power, age)
        self.letter = "F"


class Otter(Animal):
    """
    Otter class
    """

    def __init__(self, gender, power, age):
        super().__init__(gender, power, age)
        self.letter = "O"
