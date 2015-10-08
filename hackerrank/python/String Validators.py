# https://www.hackerrank.com/challenges/string-validators/

string = input()

print(string.isalnum())
for letter in string:
    if letter.isalpha(): 
        print(True)
        break
else:
    print(False)
for letter in string:
    if letter.isdigit(): 
        print(True)
        break
else:
    print(False)
for letter in string:
    if letter.islower(): 
        print(True)
        break
else:
    print(False)
for letter in string:
    if letter.isupper(): 
        print(True)
        break
else:
    print(False)
