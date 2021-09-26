"""
Thic module contains classes connected with flowers and buckets.
"""


import doctest


class Flower:
    """
    This class creates objects - flowers

    >>> tul = Flower('red', 1232, 123)
    >>> tul.color
    'red'
    """

    def __init__(self, color, petals, price):
        self.color = color
        self.petals = petals
        self.price = price
        self.corect()

    def corect(self):
        """
        This method checks if inputed data is correct.
        """
        if not isinstance(self.petals, int) or not isinstance(self.price, int):
            raise TypeError("""For petals only integers are allowed.
For price only int numbers are allowed.""")
        if self.price < 0 or self.petals < 0:
            raise Exception("Price and amount of petals shoud be >= 0")


class Tulip(Flower):
    """
    This claas creates objects tulips.

    >>> tul = Tulip(1232, 123)
    >>> tul.color
    'pink'
    """

    def __init__(self, petals, price):
        self.color = 'pink'
        super().__init__(self.color, petals, price)


class Rose(Flower):
    """
    This claas creates objects tulips.

    >>> rose = Rose(1232, 123)
    >>> rose.color
    'red'
    """

    def __init__(self, petals, price):
        self.color = 'red'
        super().__init__(self.color, petals, price)


class Chamomile(Flower):
    """
    This claas creates objects tulips.

    >>> cham = Chamomile(1232, 123)
    >>> cham.color
    'white'
    """

    def __init__(self, petals, price):
        self.color = 'white'
        super().__init__(self.color, petals, price)


class FlowerSet:
    """
    This class creates flower sets.

    >>> cham = Chamomile(1232, 123)
    >>> ros = Rose(123, 123)
    >>> set = FlowerSet()
    >>> set.add_flower(ros)
    >>> set.add_flower(cham)
    >>> len(set.flowerset)
    2
    """

    def __init__(self):
        self.flowerset = set()

    def add_flower(self, flower):
        """
        This method adds flowers to the set.
        """
        self.flowerset.add(flower)


class Bucket:
    """
    This class creates buckets of the flowersets.

    >>> cham = Chamomile(1232, 123)
    >>> ros = Rose(123, 123)
    >>> set = FlowerSet()
    >>> set.add_flower(ros)
    >>> set.add_flower(cham)
    >>> another_cham = Chamomile(1232, 123)
    >>> another_ros = Rose(123, 123)
    >>> another_set = FlowerSet()
    >>> another_set.add_flower(ros)
    >>> another_set.add_flower(cham)
    >>> bucket = Bucket()
    >>> bucket.add_set(set)
    >>> bucket.add_set(another_set)
    >>> len(bucket.bucket)
    2
    """

    def __init__(self):
        self.bucket = set()

    def add_set(self, flowerset):
        """
        This method adds sets to the bucket.

        >>> another_ros = Rose(123, 123)
        >>> another_set = FlowerSet()
        >>> another_set.add_flower(another_ros)
        >>> bucket = Bucket()
        >>> bucket.add_set(another_set)
        >>> len(bucket.bucket)
        1
        """
        self.bucket.add(flowerset)

    def total_price(self):
        """
        This method returns the whole price of the bucket.

        >>> another_ros = Rose(123, 123)
        >>> another_set = FlowerSet()
        >>> another_set.add_flower(another_ros)
        >>> bucket = Bucket()
        >>> bucket.add_set(another_set)
        >>> bucket.total_price()
        123
        """
        price = 0
        for i in self.bucket:
            for flower in i.flowerset:
                price += flower.price
        return price
