#!/bin/bash

for f in {1..26}
do
	Tests/testu01 -m rabbit -i random_numbers_time/dieharder203.bin -t $f --bit_nb 200000000 >>results_rabbit.txt
done
