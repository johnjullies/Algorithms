# https://www.hackerrank.com/challenges/sets/copy-from/13193132

result = []

n = input()
n = set(map(int, raw_input().split(' ')))
m = input()
m = set(map(int, raw_input().split(' ')))

for e in n.difference(m): result.append(e)
for e in m.difference(n): result.append(e)
for e in sorted(result): print e