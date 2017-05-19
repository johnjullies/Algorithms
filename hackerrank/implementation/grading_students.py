#!/bin/python

import sys

def solve(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            grade = round_up(grade)
            result.append(grade)
    return result
            
def round_up(grade):
    next_multiple = 40
    while next_multiple < grade:
        next_multiple += 5
    if next_multiple - grade < 3:
        grade = next_multiple
        return grade
    
    return grade

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
