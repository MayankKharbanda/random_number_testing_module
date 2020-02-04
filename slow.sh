#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt


#dieharder tests
dieharder -d 203 -f /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -g 201 > /home/mayank/Desktop/randomness/byte_stream/results_slow.txt   #rgb_lagged_sum


#change path for nist
cd /home/mayank/Desktop/randomness/Tests/NIST-Test-Suite/

#nist test
./assess 0


#change path for TestU01

cd /home/mayank/Desktop/randomness/Tests/TestU01_file/

#testu01
./testu01 -m big_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 10 >>/home/mayank/Desktop/randomness/byte_stream/results_slow.txt


./testu01 -m big_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 20 >>/home/mayank/Desktop/randomness/byte_stream/results_slow.txt


./testu01 -m big_crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 30 >>/home/mayank/Desktop/randomness/byte_stream/results_slow.txt
timestamp >> time.txt
