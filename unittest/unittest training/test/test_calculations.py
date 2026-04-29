import sys
import unittest
from pickle import FALSE

from src.calculations import add, sub, mul, div, ne

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res=add(10, 5)
        self.assertEqual(res, 15, msg='Addition Error')

    def test_sub(self):
        res=sub(10, 5)
        self.assertEqual(res, 5, msg='Subtraction Error')

    def test_mul(self):
        res=mul(10, 5)
        self.assertEqual(res, 50, msg='Multiplication Error')

    def test_div(self):
        res=div(10, 5)
        self.assertEqual(res, 2, msg='Division Error')


    @unittest.skipIf(sys.version_info>(3, 13),reason='not implemeted yet')
    def test_ne(self):
        res=ne(10, 10)
        self.assertTrue(res, msg='ne')

if __name__ == '__main__':
    unittest.main()
