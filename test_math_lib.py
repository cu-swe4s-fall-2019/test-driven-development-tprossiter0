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
        for i in range(1, 100):
            intlist = []
            for j in range(1, 10):
                intlist.append(random.randint(-50, 50))
            ret = math_lib.list_mean(intlist)
            self.assertEqual(ret, stat.mean(intlist))

    def test_list_mean_floats(self):
        for i in range(1, 100):
            flist = []
            for j in range(1, 20):
                flist.append(random.uniform(1, 100))
            ret = math_lib.list_mean(flist)
            self.assertAlmostEqual(ret, stat.mean(flist))

    def test_list_mean_combo(self):
        for i in range(1, 100):
            clist = []
            for j in range(1, 20):
                if(j % 2 == 0):
                    clist.append(random.randint(1, 100))
                else:
                    clist.append(random.uniform(1, 100))
            ret = math_lib.list_mean(clist)
            self.assertAlmostEqual(ret, stat.mean(clist))


if __name__ == '__main__':
    unittest.main()
