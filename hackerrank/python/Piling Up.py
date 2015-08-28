# https://www.hackerrank.com/challenges/piling-up

from collections import deque

for i in range(int(input())):
    n = int(input())
    sideLengths = deque(map(int, input().split()))
    
    top = max(sideLengths)
    while len(sideLengths) > 0:
        if sideLengths[0] >= sideLengths[-1] and sideLengths[0] <= top:
            top = sideLengths[0]
            sideLengths.popleft()
        elif sideLengths[-1] >= sideLengths[0] and sideLengths[-1] <= top:
            top = sideLengths[-1]
            sideLengths.pop()
        else:
            break
        
    if len(sideLengths) == 0: print("Yes")
    else: print("No")