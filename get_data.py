import sys


def read_stdin_col(col_num):
    """ Read in the values(numbers) of a specified column from stdin

    Parameters
    ----------
    col_num - column index for which we will aggregate its numbers

    Returns
    ----------
    col     - list/vector of the values in that column

    """
    if(col_num is None):
        return None

    if(isinstance(col_num, int) is False):
        raise IndexError
        sys.exit(1)

    if (col_num < 0):
        raise IndexError
        sys.exit(1)

    col = []

    try:
        for line in sys.stdin:
            nums = line.split()
            col.append(int(nums[col_num]))

    except Exception:
        print("Error in getting values from column", file=stderr)
        sys.exit(1)

    return col
