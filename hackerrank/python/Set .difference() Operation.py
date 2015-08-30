# https://www.hackerrank.com/challenges/py-set-difference-operation/

_ = input()
english = set(input().split())
_ = input()
french = set(input().split())

print(len(english - french))