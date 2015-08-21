# https://www.hackerrank.com/challenges/find-a-string

s = input()
s_ = input()

i = 0
while s.find(s_) > -1:
   s = s[s.find(s_)+1:]
   i += 1
    
print(i)