#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt


#dieharder tests
dieharder -d 203 -f /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -g 201 > /home/mayank/Desktop/randomness/byte_stream/results_fast.txt   #birthday


#change path for nist
cd /home/mayank/Desktop/randomness/Tests/NIST-Test-Suite/

#nist test
./assess 2


#change path for TestU01

cd /home/mayank/Desktop/randomness/Tests/TestU01_file/

#testu01
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 1 >>/home/mayank/Desktop/randomness/byte_stream/results_fast.txt
#smarsa birthday spacing


./testu01 -m small_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 4 >>/home/mayank/Desktop/randomness/byte_stream/results_fast.txt
#sknuth simppoker test


./testu01 -m small_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 6 >>/home/mayank/Desktop/randomness/byte_stream/results_fast.txt
#sknuth maxoft test

timestamp >> time.txt
