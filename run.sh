#!/bin/bash
file_count_normal=0
file_count_fast=0
total_count=2


cd /home/mayank/Desktop/randomness/byte_stream/
./fast.sh 0 & Process_id1=$!

cd /home/mayank/Desktop/randomness/byte_stream/
./normal.sh 0 & Process_id2=$!



while [ true ]
do

	if ! ps -p $Process_id2 > /dev/null ;
	then
		((file_count_normal=(file_count_normal+1)%total_count))
		python3 numpy-random.py random_normal_$file_count_normal.bin
		
		cd /home/mayank/Desktop/randomness/byte_stream/
		./normal.sh $file_count_normal & Process_id2=$!
		

	
	elif ! ps -p $Process_id1 > /dev/null ;
	then
		((file_count_fast=(file_count_fast+1)%total_count))
		python3 numpy-random.py random_fast_$file_count_fast.bin
		
		cd /home/mayank/Desktop/randomness/byte_stream/  
		./fast.sh $file_count_fast & Process_id1=$!

	fi
done
