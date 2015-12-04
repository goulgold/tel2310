#!/usr/bin/env python

# lookup asn number, and print result
from ipwhois import IPWhois
import re
import sys

iptest = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

def testip(str):
    if iptest.match(str):
        return True
    else:
        return False

f = open(sys.argv[1], 'r')

for line in f:
    str_list = line.split(' ')
    for str in str_list:
        if testip(str):
            try:
                asn = ''
                obj = IPWhois(str)
                results = obj.lookup()
                asn += ' ('
                asn += results['asn']
                asn += ', '
                asn += results['nets'][0]['description']
                asn += ')'
                line = line + asn
            except:
                continue
    print line,
