import unittest
import random
import statistics
import data_viz
import os.path
from os import path


class TestFileInputs(unittest.TestCase):
    def test_boxplot_filename_already_exists(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.close()

        with self.assertRaises(Exception) as ex:
            data_viz.boxplot([1, 2], test_filename)
        output = str(ex.exception)
        self.assertEqual(output, "error, file already exists")

    def test_histogram_filename_already_exists(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.close()

        with self.assertRaises(Exception) as ex:
            data_viz.histogram([1, 2], test_filename)
        output = str(ex.exception)
        self.assertEqual(output, "error, file already exists")

    def test_combo_filename_already_exists(self):
        test_filename = "test_file"
        test_file = open(test_filename, "w")
        test_file.close()

        with self.assertRaises(Exception) as ex:
            data_viz.combo([1, 2], test_filename)
        output = str(ex.exception)
        self.assertEqual(output, "error, file already exists")

    def test_boxplot_correct_filename_input(self):
        with self.assertRaises(Exception) as ex:
            data_viz.boxplot([], 123)
        output = str(ex.exception)
        self.assertEqual(output, "file name must be alphanumeric(string)")

    def test_histogram_correct_filename_input(self):
        with self.assertRaises(Exception) as ex:
            data_viz.histogram([], 123)
        output = str(ex.exception)
        self.assertEqual(output, "file name must be alphanumeric(string)")

    def test_combo_correct_filename_input(self):
        with self.assertRaises(Exception) as ex:
            data_viz.combo([], 123)
        output = str(ex.exception)
        self.assertEqual(output, "file name must be alphanumeric(string)")


if __name__ == '__main__':
    unittest.main()
