# https://www.hackerrank.com/challenges/sets/copy-from/13193132

n = input()
n = set(map(int, raw_input().split(' ')))
m = input()
m = set(map(int, raw_input().split(' ')))

result = sorted(n.difference(m).union(m.difference(n)))

for e in result: print e