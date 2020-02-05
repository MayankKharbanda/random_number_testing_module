#!/bin/bash


mkdir -p /home/mayank/Desktop/randomness/byte_stream/results/normal/$1/
mkdir -p /home/mayank/Desktop/randomness/byte_stream/results/normal/results_$1_nist/

#dieharder tests
dieharder -d 1 -f /home/mayank/Desktop/randomness/byte_stream/random_normal_$1.bin -g 201 > /home/mayank/Desktop/randomness/byte_stream/results/normal/$1/results.txt   #operm5

cd /home/mayank/Desktop/randomness/Tests/NIST-Test-Suite/

#nist test
./assess 1 $1


cd /home/mayank/Desktop/randomness/Tests/TestU01_file/
#testu01
./testu01 -m crush -i /home/mayank/Desktop/randomness/byte_stream/random_normal_$1.bin -t 1 >>/home/mayank/Desktop/randomness/byte_stream/results/normal/$1/results.txt
#smutlin multinomial test


./testu01 -m crush -i /home/mayank/Desktop/randomness/byte_stream/random_normal_$1.bin -t 19 >>/home/mayank/Desktop/randomness/byte_stream/results/normal/$1/results.txt
#snpair closepair test


./testu01 -m crush -i /home/mayank/Desktop/randomness/byte_stream/random_normal_$1.bin -t 22 >>/home/mayank/Desktop/randomness/byte_stream/results/normal/$1/results.txt
#snpair closepair bit match
