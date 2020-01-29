#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time.txt
timestamp >> time.txt
./assess 2000000
timestamp >> time.txt

