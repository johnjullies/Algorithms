# https://www.hackerrank.com/challenges/itertools-product/

from itertools import product

A = map(int, input().split())
B = map(int, input().split())

for i in product(A, B): print(i, end=" ")