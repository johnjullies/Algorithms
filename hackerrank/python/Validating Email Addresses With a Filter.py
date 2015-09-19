# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/

import re

l = []
for _ in range(int(input())):
    l.append(input())
    
print(sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$', x), l))))