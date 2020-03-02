#!/bin/bash

for f in {1..9}
do
	Tests/testu01 -m alphabit -i random_numbers_time/dieharder203.bin -t $f --bit_nb 200000000 >>results_alphabit.txt
done
