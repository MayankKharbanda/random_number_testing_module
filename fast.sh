#!/bin/bash


mkdir -p results_parallel_process/
#mkdir -p /home/mayank/Desktop/randomness/byte_stream/results/fast/results_$1_nist/

case $1 in 
	1) dieharder -d 203 -f random_numbers/dieharder_203.bin -g 201 > results_parallel_process/dieharder_203.txt   #birthday
		;;
		
	2) Tests/NIST-Test-Suite/assess 3
		;;
	
	3) Tests/TestU01_file/testu01 -m small_crush -i random_numbers/dieharder_203.bin -t 1 >> results_parallel_process/small_crush_1.txt
		#smarsa birthday spacing
		;;
	4) Tests/TestU01_file/testu01 -m small_crush -i random_numbers/dieharder_203.bin -t 4 >> results_parallel_process/small_crush_4.txt
		#sknuth simppoker test
		;;
	
	5) Tests/TestU01_file/testu01 -m small_crush -i random_numbers/dieharder_203.bin -t 6 >> results_parallel_process/small_crush_6.txt
#sknuth maxoft test
		;;
	esac

