#!/bin/bash
test_number_normal=0
test_number_fast=0
total_count=5


cd /home/mayank/Desktop/randomness/byte_stream/
./fast.sh 0 & Process_id1=$!

cd /home/mayank/Desktop/randomness/byte_stream/
./normal.sh 0 & Process_id2=$!
Time_taken=0
STARTTIME=$(date +%s)

while [ true ]
do

	if ! ps -p $Process_id2 > /dev/null ;
	then
		Time_taken=$((Time_taken+((date +%s)-STARTTIME)))
		STARTTIME=$(date +%s)
		((test_number_normal=((test_number_normal+1)%total_count))
		#generate file
		cd /home/mayank/Desktop/randomness/byte_stream/
		./normal.sh $test_number_normal & Process_id2=$!
		

	
	elif ! ps -p $Process_id1 > /dev/null ;
	then
		Time_taken=$((Time_taken+((date +%s)-STARTTIME)))
		STARTTIME=$(date +%s)
		((test_number_fast=(test_number_fast+1)%total_count))
		
		cd /home/mayank/Desktop/randomness/byte_stream/  
		./fast.sh $test_number & Process_id1=$!

	fi
done
