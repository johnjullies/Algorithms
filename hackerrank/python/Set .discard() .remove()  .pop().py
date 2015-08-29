# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/

n = int(input())
s = set(map(int, input().split())) 

for _ in range(int(input())):
    args = input().strip().split()
    
    if args[0] == "pop": 
        s.pop()
    else:
        if int(args[1]) in s:
            eval("s." + args[0] + "(" + args[1] + ")")
        
print(sum(s))  