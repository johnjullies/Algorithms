# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation

_ = input()
english = set(input().split())
_ = input()
french = set(input().split())

print(len(english ^ french))