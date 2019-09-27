import math_lib as ml
import matplotlib.pyplot as plt
import os.path
from os import path


def boxplot(L, out_file_name):
    """ Make Boxplot in an output file from the data in a numerical array

    Parameters
    ----------
    L- Array of integers and/or floats to be plotted and analyzed
    out_file_name - the name of the ouput file to which the plot,
    mean and stdev will be given

    Returns
    ----------
    No return value except for datastream to output file

    """

    if path.exists(out_file_name):
        raise Exception("error, file already exists")
    if (isinstance(out_file_name, str) is False):
        raise Exception("file name must be alphanumeric(string)")
    pass


def histogram(L, out_file_name):
    """ Make Histogram in an output file from the data in a numerical array

    Parameters
    ----------
    L- Array of integers and/or floats to be plotted and analyzed
    out_file_name - the name of the ouput file to which the plot,
    mean and stdev will be given

    Returns
    ----------
    No return value except for datastream to output file

    """
    if path.exists(out_file_name):
        raise Exception("error, file already exists")
    if (isinstance(out_file_name, str) is False):
        raise Exception("file name must be alphanumeric(string)")
    pass


def combo(L, out_file_name):
    """ Make Boxplot and Histogram in an output file from the
    data in a numerical array

    Parameters
    ----------
    L- Array of integers and/or floats to be plotted and analyzed
    out_file_name - the name of the ouput file to which the plot,
    mean and stdev will be given

    Returns
    ----------
    No return value except for datastream to output file

    """
    if path.exists(out_file_name):
        raise Exception("error, file already exists")
    if (isinstance(out_file_name, str) is False):
        raise Exception("file name must be alphanumeric(string)")
    pass
