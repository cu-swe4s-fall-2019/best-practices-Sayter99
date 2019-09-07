#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run style_test_style pycodestyle style.py
assert_no_stdout
run style_test_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run basic_stats python get_column_stats.py --file_name data.txt --column_number 2
assert_exit_code 0
run invalid_column_text python get_column_stats.py --file_name data.txt --column_number abc
assert_exit_code 1
run invalid_column python get_column_stats.py --file_name data.txt --column_number 10
assert_exit_code 1

V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

echo "...running get_column_stats.py with data.txt and 2..."
run basic_stats python get_column_stats.py --file_name data.txt --column_number 2
assert_exit_code 0
echo "...show help of get_column_stats.py..."
run help_command python get_column_stats.py -h
assert_exit_code 0

(for i in `seq 1 100`; do 
    echo -e "$RANDOM,$RANDOM,$RANDOM,$RANDOM,$RANDOM";
done )> data.txt

echo "...test get_column_stats.py with invalid file..."
run bad_file python get_column_stats.py --file_name data.txt --column_number 3
assert_exit_code 1
