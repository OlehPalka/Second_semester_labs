"""
This module contains class which makes operations with triangles.
"""

import math
import point
from typing import List


class Triangle:
    """
    This class creates triangles and does some actions with them.
    """

    def __init__(self, point_1, point_2, point_3: List[point.Point]):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def is_triangle(self):
        """
        This method checkes if it is possible to create a triangle from given points.

        >>> point_1 = point.Point(1, 1)
        >>> point_2 = point.Point(3, 2)
        >>> point_3 = point.Point(1, 2)
        >>> triangle = Triangle(point_1, point_2, point_3)
        >>> triangle.is_triangle()
        True
        """
        if self.point_1.x == self.point_2.x == self.point_3.x or self.point_1.y == \
                self.point_2.y == self.point_3.y:
            return False
        if self.point_1.x == self.point_1.y and self.point_2.x == self.point_2.y\
                and self.point_3.x == self.point_3.y:
            return False
        return True

    def perimeter(self):
        """
        This method finds perimetr of the triangle.

        >>> triangle = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        point_1_point_2 = math.sqrt(
            (self.point_2.x - self.point_1.x) ** 2 + (self.point_2.y - self.point_1.y) ** 2)
        point_2_point_3 = math.sqrt(
            (self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
        point_3_point_1 = math.sqrt(
            (self.point_1.x - self.point_3.x) ** 2 + (self.point_1.y - self.point_3.y) ** 2)
        return point_1_point_2 + point_2_point_3 + point_3_point_1

    def area(self):
        """
        This method calculates area of the triangle.

        >>> triangle = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
        >>> triangle.area()
        2.0
        """
        point_1_point_2 = math.sqrt(
            (self.point_2.x - self.point_1.x) ** 2 + (self.point_2.y - self.point_1.y) ** 2)
        point_2_point_3 = math.sqrt(
            (self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
        point_3_point_1 = math.sqrt(
            (self.point_1.x - self.point_3.x) ** 2 + (self.point_1.y - self.point_3.y) ** 2)
        half_per = self.perimeter() / 2
        area = math.sqrt(half_per * (half_per - point_1_point_2) *
                         (half_per - point_2_point_3) * (half_per - point_3_point_1))
        return area


if __name__ == "__main__":
    triangle_1 = Triangle(point.Point(
        1, 1), point.Point(3, 1), point.Point(2, 3))
    print(triangle_1.area())
