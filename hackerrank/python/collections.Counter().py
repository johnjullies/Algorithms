# https://www.hackerrank.com/challenges/collections-counter/

from collections import Counter

X = int(input())
sizes = map(int, input().split())

sizes_counts = Counter(sizes)
money = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if sizes_counts[size] > 0:
        money += price
        sizes_counts[size] -= 1

print(money)