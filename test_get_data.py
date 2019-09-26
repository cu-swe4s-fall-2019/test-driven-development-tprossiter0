import unittest
import random
import statistics as stat
import get_data as gd


class TestGetData(unittest.TestCase):
    def test_rsc_None(self):
        ret = gd.read_stdin_col(None)
        self.assertEqual(ret, None)

    def test_rsc_bad_parameters_int(self):
        with self.assertRaises(IndexError):
            ret = gd.read_stdin_col("x")

    def test_rsc_bad_parameters_float(self):
        with self.assertRaises(IndexError):
            ret = gd.read_stdin_col(1.2)

    def test_rsc_bad_parameters_negative_int(self):
        with self.assertRaises(IndexError):
            ret = gd.read_stdin_col(-10)

# testing omitted for stdin


if __name__ == '__main__':
    unittest.main()
