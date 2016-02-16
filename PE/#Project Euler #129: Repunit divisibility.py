# https://www.hackerrank.com/contests/projecteuler/challenges/euler129/copy-from/17501384

import fractions 

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

def A(n):
  x, k = 1, 1
  while x != 0:
    x = (x*10 + 1) % n
    k += 1
  return k

t = input()
for _ in range(t):
    n = input()
    print A(n)
