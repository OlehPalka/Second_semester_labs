"""
Testing module for lines intersection.
"""

from line import Point, Line
import unittest


class TestLine(unittest.TestCase):
    """
    Class which tests function from module task_1
    """

    def test_intersection(self):
        """
        This method cheks if the functtion works correctly.
        """
        line_1 = Line([Point(3, 3), Point(1, 1)])
        line_2 = Line([Point(1, 2), Point(3, 4)])
        line_3 = Line([Point(2, 2), Point(4, 4)])
        line_4 = Line([Point(1, 2), Point(3, 4)])
        line_6 = Line([Point(0, 1), Point(0, 3)])
        line_7 = Line([Point(0, 10), Point(0, 23)])
        line_8 = Line([Point(1, 5), Point(5, 5)])
        line_9 = Line([Point(-1, 5), Point(-5, 5)])
        self.assertEqual(Line, type(line_8.intersect(line_9)))
        self.assertEqual(True, line_1.__eq__(line_3))
        self.assertEqual(False, line_1.__eq__(line_4))
        self.assertEqual(False, line_1.__eq__(Point(0, 0)))
        self.assertEqual(True, Point(0, 0).__eq__(Point(0, 0)))
        self.assertEqual(False, Point(0, 0).__eq__(Point(0, 1)))
        self.assertEqual(False, Point(0, 0).__eq__(line_1))
        self.assertEqual(None, line_1.intersect(line_2))
        self.assertEqual(Line, type(line_1.intersect(line_3)))
        self.assertEqual(Line, type(line_2.intersect(line_4)))
        self.assertEqual(Line, type(line_4.intersect(line_2)))
        self.assertEqual(Point, type(line_6.intersect(line_1)))
        self.assertEqual(Point, type(line_2.intersect(line_7)))


if __name__ == "__main__":
    unittest.main()
