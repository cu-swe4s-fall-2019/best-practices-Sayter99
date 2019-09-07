# best-practices
This is the assignment for cultivating good habit while building python projects. The practices are *style correction*, *argparse utilization*, *exception handling*, and *testing*.

## Installation
To use this package, you need to have [Python3](https://www.python.org/download/releases/3.0/) in your environment.

### Used Packages
* argparse
* os
* sys
* math
* pycodestyle

## Usage
To verify the results, run `basics_test.sh` directly:
```bash
bash basics_test.sh
```

## Changes in this assignment
* To fix style issues in `style.py`, I used `pycodestyle` to detect issues and then fixed all of them.
* To make `get_column_stats.py` more robust and flexible, I utilized the `argparse` package to handle its inputs.
* Add exception handling sections in `get_column_stats.py` and test them accordingly.
    * `file not found`: verify if the input file exist
    * `value error`: verify column number is an integer
    * `index error`: verify column number is valid
* Modify the test script to demonstrate that `get_column_stats.py` conforms to the best practices
    * test with `ssshtest`
    * add tests for `exception handling` and `argparse utilization`