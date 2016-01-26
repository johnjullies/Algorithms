// https://www.hackerrank.com/contests/30-days-of-code/challenges/day-12-inheritance

class Grade(Student):
   def __init__(self, firstName, lastName, phone, score):
        Student.__init__(self, firstName, lastName, phone)
        self.score = score
   
   def calculate(self):
        if self.score < 40: return 'D'
        if self.score >= 40 and self.score < 60: return 'B'
        if self.score >= 60 and self.score < 75: return 'A'
        if self.score >= 75 and self.score < 90: return 'E'
        if self.score >= 90 and self.score <= 100: return 'O'
