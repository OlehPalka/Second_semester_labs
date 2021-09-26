"""
This module contains class which creates points.
"""


class Point:
    """
    Clas which creates points.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    point_1 = Point(1, 2)
    print(point_1.x)
