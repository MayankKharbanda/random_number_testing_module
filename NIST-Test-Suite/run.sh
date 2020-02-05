#!/bin/bash

timestamp(){
	date "+%s"
}
 : > time2.txt
timestamp >> time2.txt
./assess 2000000
timestamp >> time2.txt

