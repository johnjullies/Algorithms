# https://www.hackerrank.com/challenges/exceptions/

for _ in range(int(input())):
    try:
        a, b = map(int, input().split())    
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: " + str(e))
    except ValueError as e:
        print("Error Code: " + str(e))