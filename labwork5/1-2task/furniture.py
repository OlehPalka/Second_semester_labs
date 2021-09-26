"""
This module contains two classes furniture and chair.
They are trainings to learn Classes.
"""


class Furniture:
    """
    This class creates objectes - furniture.

    >>> furniture1 = Furniture("empire", "bedroom")
    >>> assert(furniture1.style == "empire")
    """

    def __init__(self, style, assign):
        self.style = style
        self.assign = assign

    def __str__(self):
        """
        This method reurns centence with style of furniture.

        >>> furniture1 = Furniture("empire", "bedroom")
        >>> assert(str(furniture1) == "<furniture style is empire>")
        """
        return "<furniture style is " + str(self.style) + ">"


class Chair(Furniture):
    """
    This class creates chairs.

    >>> chair1 = Chair("empire", "bedroom", "armchair")
    >>> assert(chair1.tipe == "armchair")
    """

    def __init__(self, style, assign, tipe):
        super().__init__(style, assign)
        self.tipe = tipe

    def __str__(self):
        """
        This method reurns centence with whole information given about
        the chair.

        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> assert(str(chair1) == "<This armchair furniture style is empire>")
        """
        return "<This armchair furniture style is " + str(self.style) + ">"

    def get_assign(self):
        """
        This mehod returnschair`s assign.

        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> assert(chair1.get_assign() == "bedroom")
        """
        return self.assign
