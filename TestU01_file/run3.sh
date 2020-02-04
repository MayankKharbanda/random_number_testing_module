#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time3.txt
 : > results_big_crush.txt
timestamp >> time3.txt
for f in {1..160}
do
	./testu01 -m big_crush -i /home/mayank/Desktop/randomness/Tests/TestU01/numpy-random.bin -t $f >>results_big_crush.txt
done

timestamp >> time3.txt

