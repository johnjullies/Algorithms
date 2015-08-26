# https://www.hackerrank.com/challenges/word-order

from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]
counts = Counter(words)

print(len(counts))

for word in words:
    count = counts.pop(word, None)
    if count == None:
        continue
    else:
        print(count, end = " ")