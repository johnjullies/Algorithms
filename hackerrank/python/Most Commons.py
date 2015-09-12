# https://www.hackerrank.com/challenges/most-commons

from collections import Counter
print("\n".join(i[0] + " " + str(i[1]) for i in sorted(Counter(input()).items(), key = lambda x: (-x[1],x[0]))[:3]))