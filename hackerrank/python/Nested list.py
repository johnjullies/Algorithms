# https://www.hackerrank.com/challenges/nested-list

n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
second_highest = sorted(set([marks for name, marks in marksheet]))[1]

print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))