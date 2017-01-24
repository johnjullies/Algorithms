#!/bin/python

import sys


a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0),int(b1),int(b2)]

comparison_alice = [a0 > b0, a1 > b1, a2 > b2]
comparison_bob = [a0 < b0, a1 < b1, a2 < b2]

comparison_alice_scores = [int(x) for x in comparison_alice]
comparison_bob_scores = [int(x) for x in comparison_bob]

print '%s %s' % (sum(comparison_alice_scores), sum(comparison_bob_scores))
