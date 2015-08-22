# https://www.hackerrank.com/challenges/defaultdict-tutorial

from collections import defaultdict

def getIndices(d):
    for e in d['b']: 
        if e in d['a']: 
            indices = [i + 1 for i, x in enumerate(d['a']) if x == e]
            print(' '.join([str(x) for x in indices]))
        else:
            print(-1)

if __name__ == "__main__":
    r = [int(n) for n in input().split()]
    d = defaultdict(list)

    for _ in range(r[0]):
        d['a'].append(input())
    for _ in range(r[1]):
        d['b'].append(input())

    getIndices(d)