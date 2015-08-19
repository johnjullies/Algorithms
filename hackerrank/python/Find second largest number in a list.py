# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

_ = int(input())
print(sorted(set(list(map(int, input().split()))))[-2])
