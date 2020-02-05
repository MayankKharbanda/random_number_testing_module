#!/bin/sh
. /home/mayank/Desktop/randomness/byte_stream/test2.sh hel & Process_id1=$!
while [ true ]
do
if !((ps -p $Process_id1 > /dev/null))
then
	. /home/mayank/Desktop/randomness/byte_stream/test2.sh hel & Process_id1=$!
else 
	sleep 1
fi
echo "In test"
done
