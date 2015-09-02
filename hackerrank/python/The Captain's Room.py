# https://www.hackerrank.com/challenges/py-the-captains-room

k = input()
l = map(int, raw_input().split())

s = set(l)
print (sum(s) * k - sum(l)) / (k - 1)