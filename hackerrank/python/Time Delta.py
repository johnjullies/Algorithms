# https://www.hackerrank.com/challenges/python-time-delta/

from datetime import datetime

def getDifference(t1, t2):
    a = datetime.strptime(t1, "%a %d %b %Y %X %z")
    b = datetime.strptime(t2, "%a %d %b %Y %X %z")
    return abs(int((a-b).total_seconds()))

if __name__ == "__main__":
    for _ in range(int(input())):
        t1 = input()
        t2 = input()
        print(getDifference(t1, t2))