#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt


#dieharder tests
dieharder -d 1 -f /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -g 201 > /home/mayank/Desktop/randomness/byte_stream/results_normal.txt   #operm5


#change path for nist
cd /home/mayank/Desktop/randomness/Tests/NIST-Test-Suite/

#nist test
./assess 1


#change path for TestU01

cd /home/mayank/Desktop/randomness/Tests/TestU01_file/

#testu01
./testu01 -m crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 1 >>/home/mayank/Desktop/randomness/byte_stream/results_normal.txt
#smutlin multinomial test

./testu01 -m crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 19 >>/home/mayank/Desktop/randomness/byte_stream/results_normal.txt
#snpair closepair test

./testu01 -m crush -i /home/mayank/Desktop/randomness/random_numbers/numpy-random.bin -t 22 >>/home/mayank/Desktop/randomness/byte_stream/results_normal.txt 
#snpair closepair bit match

timestamp >> time.txt
