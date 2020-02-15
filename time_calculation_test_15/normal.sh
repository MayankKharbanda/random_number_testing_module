#!/bin/bash
timestamp(){
	date "+%s"
}
 : > time_normal.txt

testNames=( " " "Frequency" "BlockFrequency" "CumulativeSums" "Runs" "LongestRun" "Rank"
			"FFT" "NonOverlappingTemplate" "OverlappingTemplate" "Universal" "ApproximateEntropy" "RandomExcursions"
			"RandomExcursionsVariant" "Serial" "LinearComplexity" )

mkdir -p results_parallel_process/nist_2/${testNames[2]}/

echo "Dieharder 1" >> time_normal.txt
timestamp >> time_normal.txt
dieharder -d 1 -f random_numbers_time/dieharder1.bin -g 201 > results_parallel_process/dieharder_1.txt   #operm5
#4*1_000_000*120 bytes
timestamp >> time_normal.txt

echo "Nist 2" >> time_normal.txt
timestamp >> time_normal.txt
Tests/NIST-Test-Suite/assess 2
	#250_000*100 bytes
timestamp >> time_normal.txt


echo "Crush 1" >> time_normal.txt
timestamp >> time_normal.txt
Tests/TestU01_file/testu01 -m crush -i random_numbers_time/crush1.bin -t 1 >> results_parallel_process/crush_1.txt
		#smutlin multinomial test
timestamp >> time_normal.txt
			
			
echo "Crush 19" >> time_normal.txt
timestamp >> time_normal.txt
Tests/TestU01_file/testu01 -m crush -i random_numbers_time/crush19.bin -t 19 >> results_parallel_process/crush_19.txt
	#snpair closepair test
timestamp >> time_normal.txt

echo "crush 22" >> time_normal.txt
timestamp >> time_normal.txt
Tests/TestU01_file/testu01 -m crush -i random_numbers_time/crush22.bin -t 22 >> results_parallel_process/crush_22.txt
	#snpair closepair bit match
timestamp >> time_normal.txt
