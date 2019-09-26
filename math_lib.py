import sys


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
    return None
