# https://www.hackerrank.com/challenges/py-set-intersection-operation

_ = input()
s = set(input().split())
_ = input()
t = set(input().split())

print(len(s & t))