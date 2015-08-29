# https://www.hackerrank.com/challenges/py-introduction-to-sets

n = input()
d_heights = set(map(int, input().split()))

average = sum(d_heights) / len(d_heights)

print(average)