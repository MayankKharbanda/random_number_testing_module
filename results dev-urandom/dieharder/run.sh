#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
dieharder -a -f dev-random.bin -g 201 > results_dieharder.txt
timestamp >> time.txt
