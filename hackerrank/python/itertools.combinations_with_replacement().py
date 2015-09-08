# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/

from itertools import combinations_with_replacement

S, k = input().split()

for i in list(combinations_with_replacement(sorted(S), int(k))): print(''.join(i))