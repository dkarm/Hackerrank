#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]

if n % 2 ==1:
    n += 1

if m % 2 ==1:
    m += 1

print (n/2) * (m/2)