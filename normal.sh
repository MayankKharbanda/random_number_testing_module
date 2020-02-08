#!/bin/bash


mkdir -p results_parallel_process/
#mkdir -p /home/mayank/Desktop/randomness/byte_stream/results/normal/results_$1_nist/


case $1 in 

	1) dieharder -d 1 -f random_numbers/dieharder_1.bin -g 201 > results_parallel_process/dieharder_1.txt   #operm5
	;;

	2) Tests/NIST-Test-Suite/assess 2

	;;
	
	3) Tests/TestU01_file/testu01 -m crush -i random_numbers/dieharder_203.bin -t 1 >> results_parallel_process/crush_1.txt
		#smutlin multinomial test
	;;
	
	4) Tests/TestU01_file/testu01 -m crush -i random_numbers/dieharder_203.bin -t 19 >> results_parallel_process/crush_19.txt
	#snpair closepair test
	;;

	5) Tests/TestU01_file/testu01 -m crush -i random_numbers/dieharder_203.bin -t 22 >> results_parallel_process/crush_22.txt
	#snpair closepair bit match
	;;
	
	esac
