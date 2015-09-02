# https://www.hackerrank.com/challenges/py-check-subset

for i in range(int(input())): #More than 4 lines will result in 0 score. Do not leave a blank line also. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(A <= B)