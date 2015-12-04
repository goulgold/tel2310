#!/usr/bin/env python
import sys

# print data of one website

state = ''
website = ['www.google.com', 'www.baidu.com', 'www.amazon.com', 'www.pitt.edu', 'www.bbc.com']

def changewebsite(str, wesite, state):
    for name in website:
        if str.find(name) != -1:
            return name
    return state

testwebsite = sys.argv[1]
state = testwebsite
f = open('result_snapshot1.log', 'r')
for line in f:
    state = changewebsite(line, website, state)
    if state == testwebsite:
        print line
