import random
import math_lib
import unittest
import statistics


class TestMathLib(unittest.TestCase):
    def test_list_mean_none(self):
        ret = math_lib.list_mean(None)
        self.assertEqual(ret, None)

    def test_list_mean_empty(self):
        emptylist = []
        ret = math_lib.list_mean(emptylist)
        self.assertEqual(ret, None)


if __name__ == '__main__':
    unittest.main()
