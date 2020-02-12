#!/bin/bash
timestamp(){
	date "+%s"
}
 : > time_slow.txt

testNames=( " " "Frequency" "BlockFrequency" "CumulativeSums" "Runs" "LongestRun" "Rank"
			"FFT" "NonOverlappingTemplate" "OverlappingTemplate" "Universal" "ApproximateEntropy" "RandomExcursions"
			"RandomExcursionsVariant" "Serial" "LinearComplexity" )

mkdir -p results_parallel_process/nist_8/${testNames[8]}/

echo "Dieharder 1" >> time_slow.txt
timestamp >> time_slow.txt
dieharder -d 203 -n 31 -f random_numbers_time/dieharder203.bin -g 201 > results_parallel_process/dieharder_203.txt   
timestamp >> time_slow.txt


echo "Nist 8" >> time_slow.txt
timestamp >> time_slow.txt
Tests/NIST-Test-Suite/assess 8
	#250_000*100 bytes
timestamp >> time_slow.txt

echo "Big Crush 1" >> time_slow.txt
timestamp >> time_slow.txt
Tests/TestU01_file/testu01 -m big_crush -i random_numbers_time/bigcrush1.bin -t 1 >> results_parallel_process/big_crush_1.txt
		#smutlin multinomial test
timestamp >> time_slow.txt

echo "Big Crush 22" >> time_slow.txt
timestamp >> time_slow.txt
Tests/TestU01_file/testu01 -m big_crush -i random_numbers_time/bigcrush22.bin -t 22 >> results_parallel_process/big_crush_22.txt
		#smutlin multinomial test
timestamp >> time_slow.txt


echo "Big Crush 54" >> time_slow.txt
timestamp >> time_slow.txt
Tests/TestU01_file/testu01 -m big_crush -i random_numbers_time/bigcrush54.bin -t 54 >> results_parallel_process/big_crush_54.txt
		#smutlin multinomial test
timestamp >> time_slow.txt

