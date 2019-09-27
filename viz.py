import argparse
import sys
import math_lib
import get_data
import data_viz


def main():
    parser = argparse.ArgumentParser(
                description="plot data from stdin")

    parser.add_argument('--out_file_name',
                        type=str,
                        help='name of output file',
                        required=True)

    parser.add_argument('--plot_type',
                        type=string,
                        help='take "histrogram" or "boxplot" or "combo"',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='column num in stdin to get data from',
                        required=True)

    args = parser.parse_args()

    try:
        data = get_data(args.col_num)
    except Exception:
        print("something went wrong in get_data")
        sys.exit(1)

    if(argparse.plot_type == "boxplot"):
        try:
            data_viz.boxplot(data, args.out_file_name)
        except Exception:
            print("something went wrong in data_viz.boxplot")
            sys.exit(1)

    if(argparse.plot_type == "histogram"):
        try:
            data_viz.histogram(data, args.out_file_name)
        except Exception:
            print("something went wrong in data_viz.histogram")
            sys.exit(1)

    if(argparse.plot_type == "boxplot"):
        try:
            data_viz.combo(data, args.out_file_name)
        except Exception:
            print("something went wrong in data_viz.combo")
            sys.exit(1)
    pass


if __name__ == '__main__':
    main()
