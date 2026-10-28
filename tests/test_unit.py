import unittest
from src.Converter import Converter

class test_unit(unittest.TestCase):
    def test_100_7_up(self):
        self.assertEqual(Converter.do(100.9), 1000)
    def test_100_7(self):
        self.assertEqual(Converter.do(100.7), 1000)
    def test_0_100_7(self):
        self.assertEqual(Converter.do(50.5), 50)
    def test_0(self):
        self.assertEqual(Converter.do(0), ValueError)
    def test_between_min_30_4_0(self):
        self.assertEqual(Converter.do(-10.5), -10)
    def test_min_30_4(self):
        self.assertEqual(Converter.do(-30.4), -30)
    def test_below_min_30_5(self):
        self.assertEqual(Converter.do(-59.5), -59)
    def test_min_30_5(self):
        self.assertEqual(Converter.do(-30.5), -30)
    def test_min_30_45(self):
        self.assertEqual(Converter.do(-30.45), ValueError)
