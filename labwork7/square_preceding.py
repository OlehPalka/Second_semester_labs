"""
this module contains function which makes squaring of items in list
"""


def square_preceding(values):
    """ (list of number) -> NoneType
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    try:
        if values != []:
            temp = values[0]
            values[0] = 0
        for i in range(1, len(values)):
            next_temp = values[i]
            values[i] = temp ** 2
            temp = next_temp
    except TypeError:
        return "One of symbols you entered is not int or float."
