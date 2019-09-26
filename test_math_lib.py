import random
import math_lib
import unittest
import statistics as stat


class TestMathLib(unittest.TestCase):
    def test_list_mean_none(self):
        ret = math_lib.list_mean(None)
        self.assertEqual(ret, None)

    def test_list_mean_empty(self):
        emptylist = []
        ret = math_lib.list_mean(emptylist)
        self.assertEqual(ret, None)

    def test_list_mean_ints(self):
        intlist = [1, 2, 3, 4, 5, 6, -1, -5, -50]
        ret = math_lib.list_mean(intlist)
        self.assertEqual(ret, stat.mean(intlist))


if __name__ == '__main__':
    unittest.main()
