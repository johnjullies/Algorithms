# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/

def mobile(function):
    def input(number):
            return sorted([function(i) for i in number])
    return input

@mobile
def standardize(n):
    return "+91 " + n[-10:-5] + " " + n[-5:]

number = list()
for _ in range(int(input())):
    number.append(input())

print('\n'.join(standardize(number)))