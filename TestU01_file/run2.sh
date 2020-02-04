#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time2.txt
 : > results_crush.txt
timestamp >> time2.txt
for f in {1..96}
do
	./testu01 -m crush -i /home/mayank/Desktop/randomness/Tests/TestU01/python-random-updated.bin -t $f >>results_crush.txt
done

timestamp >> time2.txt

