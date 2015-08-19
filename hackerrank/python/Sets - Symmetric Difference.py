# https://www.hackerrank.com/challenges/sets/copy-from/13193132

n = int(input())
n = set(map(int, input().split()))
m = int(input())
m = set(map(int, input().split()))

for e in sorted(n.difference(m).union(m.difference(n))): print(e)