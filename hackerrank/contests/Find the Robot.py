# https://www.hackerrank.com/contests/w17/challenges/find-the-robot/

x, y, d = 0, 0, 0

for _ in range(int(input())):
    N = int(input())
    for i in range(1, N+1):
        if d > 3: d = 0
        
        if d == 0: x += i
        elif d == 1: y += i
        elif d == 2: x -= i
        elif d == 3: y -= i
            
        d += 1
        
    print(str(x) + ' ' + str(y))
    x, y, d = 0, 0, 0