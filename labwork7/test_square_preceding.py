from square_preceding import square_preceding
import unittest


class TestSquare(unittest.TestCase):
    """
    Class which tests function from module task_1
    """

    def test_squaring(self):
        """
        This method cheks if the functtion works correctly.
        """
        self.assertEqual(None, square_preceding([1, 2, 3]))
        self.assertEqual("One of symbols you entered is not int or float.",
                         square_preceding([1, 2, 3, "d", 1]))
