# https://www.hackerrank.com/challenges/python-mutations

s = input()
args = input().split()

l = list(s)
l[int(args[0])] = args[1]

print(''.join(l))