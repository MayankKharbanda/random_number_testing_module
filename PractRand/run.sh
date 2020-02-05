#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
cat python-random-updated.bin | ./RNG_test stdin32 -a
timestamp >> time.txt

