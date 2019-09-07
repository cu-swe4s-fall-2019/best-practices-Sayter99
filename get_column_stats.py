"""Get Column Stats
    this program will show both mean and stdev of a column of the input file
    Parameters
    ----------
    --file_name : the name of the file
    --column_number : the target column

    Returns
    -------
    mean : mean of the column
    stdev: standard deviation of the column
"""
import sys
import math
import argparse


# parse arguments (file_name, column_number)
def parse_args():
    parser = argparse.ArgumentParser(
                description='The right way to pass parameters.',
                prog='get_column_stats')

    # require file name as one of the inputs
    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)

    # require column number as one of the inputs
    parser.add_argument('--column_number',
                        type=str,
                        help='The column number',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    # get argument by arg parser
    args = parse_args()
    # verify the input col_num is an integer
    col_num = None
    try:
        col_num = int(args.column_number)
    except ValueError:
        print('Please enter an integer')
        sys.exit(1)

    # check whether the file is valid
    file_name = args.file_name
    f = None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    V = []

    # fill numbers of the input column into V
    for l in f:
        # check the file format
        try:
            A = [int(x) for x in l.split()]
        except ValueError:
            print('Bad format of the input file')
            sys.exit(1)
        # check the column number is valid or not
        try:
            V.append(A[col_num])
        except IndexError:
            print('Invalid Column Number')
            sys.exit(1)

    # deal with empty V and calculate (mean, stdev)
    if (len(V) != 0):
        mean = sum(V)/len(V)
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    else:
        mean = 0
        stdev = 0

    # show results
    print('mean:', mean)
    print('stdev:', stdev)
    sys.exit()
