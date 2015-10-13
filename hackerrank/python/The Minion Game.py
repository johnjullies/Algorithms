# https://www.hackerrank.com/challenges/the-minion-game/

S = input()
N = len(S)
kevin, stuart = 0, 0

for i in range(N):
    if S[i] in 'AEIOU': kevin += (N - i)
    else: stuart += (N - i)
    
if kevin > stuart:
    print("Kevin", kevin)
elif stuart > kevin:
    print("Stuart", stuart)
else:
    print("Draw")
