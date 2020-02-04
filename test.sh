#!/bin/sh
export var1="1"
var1=$(. /home/mayank/Desktop/randomness/byte_stream/test2.sh &)
echo "$var1 in test"
sleep 5
echo "$var1 in test"
