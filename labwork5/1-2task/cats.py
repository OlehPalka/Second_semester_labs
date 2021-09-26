"""
This module contains two classes Animal and Cat.
"""


class Animal:
    """
    This class creates animals.

    >>> animal1 = Animal("chordata", "mammalia")
    >>> assert(animal1.phylum == "chordata")

    >>> assert(animal1.clas == "mammalia")

    """

    def __init__(self, phylum, clas):
        self.phylum = phylum
        self.clas = clas

    def __str__(self):
        """
        This method creates centence with information about the object.


        >>> animal1 = Animal("chordata", "mammalia")
        >>> assert(str(animal1) == "<animal class is mammalia>")
        """
        return "<animal class is " + str(self.clas) + ">"


def __eq__(self, obj):
    """
    Redefining == method.
    """
    if isinstance(obj, Animal) and self.phylum == obj.phylum and self.clas == obj.clas:
        return True
    else:
        return False


class Cat(Animal):
    """
    This class creates cats.

    >>> cat1 = Cat("chordata", "mammalia", "felis")
    >>> assert(cat1.sound() == "Meow")
    >>> assert(cat1.genus == "felis")
    >>> assert(isinstance(cat1, Animal))
    >>> assert(str(cat1) == "<This felis animal class is mammalia>")
    """

    def __init__(self, phylum, clas, genus):
        super().__init__(phylum, clas)
        self.genus = genus

    def __str__(self):
        """"
        This method returnscentence about the specification of the cat.

        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> assert(str(cat1) == "<This felis animal class is mammalia>")
        """
        return "<This " + str(self.genus) + " animal class is " + str(self.clas) + ">"

    def sound(self):
        """
        This method reurns sound of the cat.

        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> assert(cat1.sound() == "Meow")
        """
        return "Meow"


if __name__ == "__main__":
    animal1 = Animal("chordata", "mammalia")

    animal2 = Animal("chordata", "birds")

    assert(not (animal1 == animal2))
