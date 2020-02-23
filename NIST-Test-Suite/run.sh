#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
./assess 8 data/nist.txt
timestamp >> time.txt

