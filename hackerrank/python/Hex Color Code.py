# https://www.hackerrank.com/challenges/hex-color-code/

import re
    
for _ in range(int(input())):
    matches = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}[;|,|\)]', input())
    for i in matches: print(i[:-1])