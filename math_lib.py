import sys
import math
import statistics as stat
import numpy as np


def list_mean(L):
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
    if L is None:
        return None
    if len(L) == 0:
        return None

    try:
        mean = list_mean(L)
        rstdev = (sum([math.pow((mean-x), 2) for x in L]) / (len(L) - 1))
        rstdev = math.sqrt(rstdev)
        # needed to add n-1
    except Exception:
        raise Exception("Something went wrong with computation")

    return rstdev
