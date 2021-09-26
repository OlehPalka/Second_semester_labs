"""
This module contains my first Class, which makes simple operations.
"""


import doctest


class Markets:
    """
    This class makes creates objects - markets.

    >>> market_family_food.name
    'Family Food'
    >>> print(market_family_food)
    Supermarket Family Food has an area of 80 m2 and has the following\
 categories: Bread and Bakery, Dairy, Beverages.
    """

    def __init__(self, name, area, categories):
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self):
        """
        THis function converts inputed information to the complete santence.
        """
        return "Supermarket " + self.name + \
            " has an area of " + str(self.area) + \
            " m2 and has the following categories: " + \
            str(", ".join(self.categories)) + "."


if __name__ == "__main__":
    market_family_food = Markets(
        'Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
    print(market_family_food.name)

    print(market_family_food.area)

    print(market_family_food.categories)

    print(market_family_food)
print(doctest.testmod())
