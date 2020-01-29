#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 1 >results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 2 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 3 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 4 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 5 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 6 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 7 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 8 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 9 >>results.txt
./testu01 -m small_crush -i /home/mayank/Desktop/randomness/TestU01/TestU01-1.2.3/examples/dev-random.bin -t 10 >>results.txt
timestamp >> time.txt

