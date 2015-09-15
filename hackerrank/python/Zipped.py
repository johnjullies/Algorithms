# https://www.hackerrank.com/challenges/zipped/

N, X = map(int, input().split())

l = []
for _ in range(X):
    l.append(list(map(float, input().split())))
    
for i in zip(*l):
    print(sum(i) / X)