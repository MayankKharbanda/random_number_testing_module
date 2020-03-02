#!/bin/bash
timestamp(){
	date "+%s"
}
 : > time_fast.txt
 
testNames=( " " "Frequency" "BlockFrequency" "CumulativeSums" "Runs" "LongestRun" "Rank"
			"FFT" "NonOverlappingTemplate" "OverlappingTemplate" "Universal" "ApproximateEntropy" "RandomExcursions"
			"RandomExcursionsVariant" "Serial" "LinearComplexity" )


mkdir -p results_parallel_process/nist_3/${testNames[3]}/

echo "Dieharder 0" >> time_fast.txt
timestamp >> time_fast.txt

dieharder -d 0 -f random_numbers_time/dieharder0.bin -g 201 > results_parallel_process/dieharder_0.txt   #birthday 
#4*1_000_00*150 bytes

timestamp >> time_fast.txt

		
echo "Nist 3" >> time_fast.txt
timestamp >> time_fast.txt
Tests/NIST-Test-Suite/assess 3
#250_000*100 bytes
timestamp >> time_fast.txt


echo "small_crush 1" >>time_fast.txt	
timestamp >> time_fast.txt
Tests/TestU01_file/testu01 -m small_crush -i random_numbers_time/smallcrush1.bin -t 1 >> results_parallel_process/small_crush_1.txt
#smarsa birthday spacing
timestamp >> time_fast.txt

echo "small_crush 4" >>time_fast.txt
timestamp >> time_fast.txt	
Tests/TestU01_file/testu01 -m small_crush -i random_numbers_time/smallcrush4.bin -t 4 >> results_parallel_process/small_crush_4.txt
#sknuth simppoker test
timestamp >> time_fast.txt


echo "small_crush 6" >>time_fast.txt	
timestamp >> time_fast.txt
Tests/TestU01_file/testu01 -m small_crush -i random_numbers_time/smallcrush6.bin -t 6 >> results_parallel_process/small_crush_6.txt
#sknuth maxoft test
timestamp >> time_fast.txt
