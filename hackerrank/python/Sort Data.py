# https://www.hackerrank.com/challenges/python-sort-sort/

N, M = map(int, input().split())

l = []
for _ in range(N):
    l.append(list(map(int, input().split())))
    
k = int(input())    

print("\n".join(list(map(lambda x: " ".join(list(map(str, x))), sorted(l, key = lambda x: x[k])))))