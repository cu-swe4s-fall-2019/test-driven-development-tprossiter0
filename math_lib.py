import sys
import math
import statistics as stat
import numpy as np


def list_mean(L):
    """ Compute arithmetic mean of a vector/list

    Parameters
    ----------
    L - takes vector of integers or floats

    Returns
    ----------
    avg - arithmetic mean of L

    """
    if L is None:
        return None
    if len(L) == 0:
        return None

    s = 0

    for i in L:
        if(((isinstance(i, int)) or (isinstance(i, float))) is False):
            raise Exception("Vals in list != ints or floats")
            sys.exit(1)

    try:
        avg = sum(L) / len(L)
    except Exception:
        print("Something went wrong with computation of mean")
        sys.exit(1)

    return(avg)


def list_stdev(L):

    """ Compute standard deviation of a vector/list

    Parameters
    ----------
    L - takes vector of integers or floats

    Returns
    ----------
    stdev - standard deviation of the L

    """

    if L is None:
        return None
    if len(L) == 0:
        return None

    try:
        # exceptions with parameters caught below by ref to list_mean()
        mean = list_mean(L)
        rstdev = (sum([math.pow((mean-x), 2) for x in L]) / (len(L) - 1))
        rstdev = math.sqrt(rstdev)
        # needed to add n-1
    except Exception:
        raise Exception("Something went wrong with computation")
        sys.exit(1)

    return rstdev
