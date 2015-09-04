# https://www.hackerrank.com/challenges/py-check-strict-superset

A = set(map(int, input().split()))
for _ in range(int(input())):
    X = set(map(int, input().split()))
    if A.issuperset(X) != True or len(A) == len(X): 
        print(False)
        break 
else: print(True)