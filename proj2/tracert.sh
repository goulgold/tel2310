#!/bin/bash
# trace route 5 website and record them in log files.

site=("www.google.com" "www.pitt.edu" "www.baidu.com" "www.bbc.com" "www.amazon.com")

date +%c
for var in ${site[@]}; do
    traceroute -n $var
done
