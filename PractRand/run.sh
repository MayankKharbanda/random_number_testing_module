#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
cat dev-random.bin | ./RNG_test stdin32 -a
timestamp >> time.txt

