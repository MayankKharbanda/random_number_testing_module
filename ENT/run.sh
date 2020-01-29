#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
./ent -b dev-random.bin > results_ent.txt
timestamp >> time.txt
