#!/bin/bash

#dieharder tests
dieharder -d 203 -f /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -g 201 > /home/mayank/Desktop/randomness/byte_stream/results_slow.txt   #rgb_lagged_sum


#nist test
. /home/mayank/Desktop/randomness/Tests/NIST-Test-Suite/assess 0
#decls.h output location


#testu01
. /home/mayank/Desktop/randomness/Tests/TestU01_file/testu01 -m big_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 10 >>/home/mayank/Desktop/randomness/byte_stream/results_slow.txt


. /home/mayank/Desktop/randomness/Tests/TestU01_file/testu01 -m big_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 20 >>/home/mayank/Desktop/randomness/byte_stream/results_slow.txt


. /home/mayank/Desktop/randomness/Tests/TestU01_file/testu01 -m big_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 30 >>/home/mayank/Desktop/randomness/byte_stream/results_slow.txt
