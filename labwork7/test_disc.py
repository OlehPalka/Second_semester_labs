from disc import *
import unittest


class TestDisc(unittest.TestCase):
    """
    Class which tests function from module disc
    """

    def test_squaring(self):
        """
        This method cheks if the functtion works correctly.
        """

        self.assertTrue(str(Disc(Center(5, 5), 4)) ==
                        "(x-5.00)**2 + (y-5.00)**2 = 16.00")
        self.assertTrue(str(Disc(Center(0, 3), 1)) ==
                        "(x)**2 + (y-3.00)**2 = 1.00")
        self.assertTrue(str(Center(1, 4)) == "Center is x=1, y=4")

        disc1 = Disc(Center(1, 1), 3)
        self.assertTrue(str(disc1) == "(x-1.00)**2 + (y-1.00)**2 = 9.00")

        self.assertTrue(disc1.radius == 3)
        self.assertTrue(isinstance(disc1.radius, int), True)

        self.assertTrue(disc1.center == (1, 1))
        disc2 = Disc(Center(5, 5), 4)
        self.assertTrue(str(disc2) == "(x-5.00)**2 + (y-5.00)**2 = 16.00")
        self.assertTrue(disc2.radius == 4)
        self.assertTrue(disc2.center == (5, 5))

        self.assertTrue(Disc(Center(0, 1), 1).is_touching(Disc(Center(0, 0), 2),
                                                          precision=PRECISION))
        self.assertTrue(not disc1.is_touching(disc2, precision=PRECISION))
        self.assertTrue(str(Disc(Center(0, 3), 1)) ==
                        "(x)**2 + (y-3.00)**2 = 1.00")
        self.assertTrue(str(Disc(Center(0, 3), 1)) ==
                        "(x)**2 + (y-3.00)**2 = 1.00")
