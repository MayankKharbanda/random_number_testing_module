#!/bin/bash


mkdir -p /home/mayank/Desktop/randomness/byte_stream/results/fast/$1/
mkdir -p /home/mayank/Desktop/randomness/byte_stream/results/fast/results_$1_nist/

#dieharder tests
dieharder -d 203 -f /home/mayank/Desktop/randomness/byte_stream/random_fast_$1.bin -g 201 > /home/mayank/Desktop/randomness/byte_stream/results/fast/$1/results.txt   #birthday


cd /home/mayank/Desktop/randomness/Tests/NIST-Test-Suite/
#nist test
./assess 2 $1

cd /home/mayank/Desktop/randomness/Tests/TestU01_file/
#testu01
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/byte_stream/random_fast_$1.bin -t 1 >>/home/mayank/Desktop/randomness/byte_stream/results/fast/$1/results.txt
#smarsa birthday spacing

./testu01 -m small_crush -i /home/mayank/Desktop/randomness/byte_stream/random_fast_$1.bin -t 4 >>/home/mayank/Desktop/randomness/byte_stream/results/fast/$1/results.txt
#sknuth simppoker test

./testu01 -m small_crush -i /home/mayank/Desktop/randomness/byte_stream/random_fast_$1.bin -t 6 >>/home/mayank/Desktop/randomness/byte_stream/results/fast/$1/results.txt
#sknuth maxoft test

