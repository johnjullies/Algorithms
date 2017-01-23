#!/bin/python

import sys


t = int(raw_input().strip())
for i in xrange(t):
    height = 1
    cycles = int(raw_input().strip())
        
    for cycle in xrange(cycles):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1
            
    print height
