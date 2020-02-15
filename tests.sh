#!/bin/bash

testNames=( " " "Frequency" "BlockFrequency" "CumulativeSums" "Runs" "LongestRun" "Rank"
			"FFT" "NonOverlappingTemplate" "OverlappingTemplate" "Universal" "ApproximateEntropy" "RandomExcursions"
			"RandomExcursionsVariant" "Serial" "LinearComplexity" )

mkdir -p results_parallel_process/nist_3/${testNames[3]}/
mkdir -p results_parallel_process/nist_2/${testNames[2]}/
mkdir -p results_parallel_process/nist_8/${testNames[8]}/

case $1 in 

	1) Tests/dieharder -d 0 -f random_numbers_time/dieharder0.bin -g 201 > results_parallel_process/dieharder_0.txt   #birthday 
	#4*1_000_00*150 bytes
	;;
	
	2) Tests/nist 3
	#250_000*100 bytes
	;;
	
	3) Tests/testu01 -m small_crush -i random_numbers_time/smallcrush1.bin -t 1 >> results_parallel_process/small_crush_1.txt
	;;
	
	4) Tests/testu01 -m small_crush -i random_numbers_time/smallcrush4.bin -t 4 >> results_parallel_process/small_crush_4.txt
		#sknuth simppoker test
	;;
	
	5) Tests/testu01 -m small_crush -i random_numbers_time/smallcrush6.bin -t 6 >> results_parallel_process/small_crush_6.txt
	;;
	
	6) Tests/dieharder -d 1 -f random_numbers_time/dieharder1.bin -g 201 > results_parallel_process/dieharder_1.txt   #operm5
	#4*1_000_000*120 bytes
	;;
	
	7) Tests/nist 2
	#250_000*100 bytes
	;;
	
	8) Tests/testu01 -m crush -i random_numbers_time/crush1.bin -t 1 >> results_parallel_process/crush_1.txt
	;;
	
	9) Tests/testu01 -m crush -i random_numbers_time/crush19.bin -t 19 >> results_parallel_process/crush_19.txt
	#snpair closepair test
	;;
	
	10) Tests/testu01 -m crush -i random_numbers_time/crush22.bin -t 22 >> results_parallel_process/crush_22.txt
	#snpair closepair bit match
	;;
	
	11) Tests/dieharder -d 203 -n 31 -f random_numbers_time/dieharder203.bin -g 201 > results_parallel_process/dieharder_203.txt   #birthday 
	#4*1_000_00*150 bytes
	;;
	
	12) Tests/nist 8
	#250_000*100 bytes
	;;
	
	13) Tests/testu01 -m big_crush -i random_numbers_time/bigcrush1.bin -t 1 >> results_parallel_process/big_crush_1.txt
	;;
	
	14) Tests/testu01 -m big_crush -i random_numbers_time/bigcrush22.bin -t 22 >> results_parallel_process/big_crush_22.txt
		#smutlin multinomial test
	;;
	
	15) Tests/testu01 -m big_crush -i random_numbers_time/bigcrush54.bin -t 54 >> results_parallel_process/big_crush_54.txt
	;;
	
	esac

