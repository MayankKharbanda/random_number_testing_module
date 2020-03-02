#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
 : > results_small_crush.txt
timestamp >> time.txt
for f in {1..10}
do
	./testu01 -m small_crush -i /home/mayank/Desktop/randomness/Tests/TestU01/python-random-updated.bin -t $f >>results_small_crush.txt
done

timestamp >> time.txt
