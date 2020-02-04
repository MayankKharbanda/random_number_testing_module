#!/bin/bash

cd /home/mayank/Desktop/randomness/byte_stream/
./fast.sh & Process_id1=$!

#echo "fast completed!!!"

cd /home/mayank/Desktop/randomness/byte_stream/
./normal.sh & Process_id2=$!

#echo "normal completed!!!"

#cd /home/mayank/Desktop/randomness/byte_stream/
#./slow.sh & Process_id3=$!
#echo "slow completed!!!"
while [ true ]
do
	wait $Process_id2 && echo "Normal completed" && exit 0 || echo "Not completed"
done
