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


def get_mean(V):
    # verify the input is a list containing only numbers
    if (isinstance(V, list)):
        for i in V:
            if not (isinstance(i, int) or isinstance(i, float)):
                print('Please input a list containing numbers')
                return None
    # if it is an empty list, return None
    if (len(V) == 0):
        print('Empty list')
        return None
    # return mean
    return float(sum(V)) / float(len(V))


def get_stdev(V):
    # verify the input is a list containing only numbers
    if (isinstance(V, list)):
        for i in V:
            if not (isinstance(i, int) or isinstance(i, float)):
                print('Please input a list containing numbers')
                return None
    # if it is an empty list, return None
    if (len(V) == 0):
        print('Empty list')
        return None
    # if mean is None, return None
    mean = get_mean(V)
    if mean is None:
        return None
    _sum = float(sum([(float(mean)-float(x))**2 for x in V]))
    return math.sqrt(_sum / float(len(V)-1))


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

    # show results
    print('mean:', get_mean(V))
    print('stdev:', get_stdev(V))
    sys.exit()
