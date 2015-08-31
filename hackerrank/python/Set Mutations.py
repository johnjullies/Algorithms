# https://www.hackerrank.com/challenges/py-set-mutations

_ = input()
A = set(map(int, input().split()))

for i in range(int(input())):
    cmd = input().split()[0]
    other_set = set(map(int, input().split()))
    eval("A." + cmd + "(other_set)")
    
print(sum(A))