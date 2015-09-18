# https://www.hackerrank.com/challenges/map-and-lambda-expression/

n = int(input())
fibo = [0, 1]

for _ in range(n): 
    fibo.append(fibo[-1] + fibo[-2])        
    
print(list(map(lambda a: a**3, fibo))[:n])