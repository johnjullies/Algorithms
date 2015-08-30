# https://www.hackerrank.com/challenges/py-set-union

n = input()
s = set(input().split())
n = input()
t = set(input().split())

print(len(s | t))