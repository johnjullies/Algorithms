# https://www.hackerrank.com/challenges/angry-professor

def checkClassStatus(nk, t):
    onTime = 0
    for e in t: 
        if e <= 0: onTime += 1
    
    if onTime >= nk[1]: return "NO"
    else: return "YES"
        
if __name__ == "__main__":
    for _ in range(int(input())):
        nk = list(map(int, input().split()))
        t = list(map(int, input().split()))
        
        print(checkClassStatus(nk, t))