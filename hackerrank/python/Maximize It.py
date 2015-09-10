# https://www.hackerrank.com/challenges/maximize-it/

from itertools import product

K, M = map(int, input().split())

n = []
for _ in range(K):
     n.append(list(map(int, input().split()))[1:])        

MAX = 0
for i in product(*n):
    MAX = max(sum(map(lambda x: x**2, i)) % M, MAX)

print(MAX)  