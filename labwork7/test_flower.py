"""This is testing module"""
import unittest
from flower import *


class TestFlower(unittest.TestCase):
    """
    Class which tests function from module task_1
    """

    def test_flower(self):
        """
        This method cheks if the function works correctly.
        """
        flower_1 = Flower("red", 10, 120)
        try:
            flower_2 = Flower("red", "10", 120)
        except Exception:
            flower_2 = "exception"
        self.assertEqual("red", flower_1.color)
        self.assertEqual(120, flower_1.price)
        self.assertEqual("exception",
                         flower_2)
        flower_3 = Tulip(12, 230)
        flower_4 = Rose(23, 40)
        flower_5 = Chamomile(13, 65)
        self.assertEqual("pink", flower_3.color)
        self.assertEqual("red", flower_4.color)
        self.assertEqual(65, flower_5.price)

    def test_set(self):
        """
        This method cheks set function.
        """
        flower_1 = Flower("red", 10, 120)
        flower_2 = Flower("red", 10, 120)
        set_flower = FlowerSet()
        set_flower.add_flower(flower_2)
        set_flower.add_flower(flower_1)
        self.assertEqual(2, len(set_flower.flowerset))

    def test_bucket(self):
        """
        This function cheks if the bucket function works properly.
        """
        flower_1 = Flower("red", 10, 120)
        flower_2 = Flower("red", 10, 120)
        set_flower = FlowerSet()
        set_flower.add_flower(flower_2)
        set_flower.add_flower(flower_1)
        bucket = Bucket()
        bucket.add_set(set_flower)
        self.assertEqual(1, len(bucket.bucket))
        self.assertEqual(240, bucket.total_price())


unittest.main()
