# https://www.hackerrank.com/challenges/re-sub-regex-substitution

import re

for _ in range(int(input())):
    string = re.sub(r'(?<= )&&(?= )', 'and', input())
    string = re.sub(r'(?<= )\|\|(?= )', 'or', string)
    print(string)