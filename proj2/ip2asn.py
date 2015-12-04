#!/usr/bin/env python

# lookup asn number, and print result
import pyasn
import re

iptest = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

ip1 = '192.168.1.1'

if iptest.match(ip1):
    print 'true'
else:
    print 'false'

f = open('result.log', 'r')

str_list = f.readline().split(' ')
str_list = f.readline().split(' ')
str_list = f.readline().split(' ')

print str_list
