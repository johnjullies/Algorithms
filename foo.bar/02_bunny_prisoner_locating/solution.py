def answer(x, y):
      base = [1]
      row = y
      col = x
      
      while row > 1:
          row -= 1
          col += 1
          
      while len(base) < col - 1:
          base.append(base[-1] + (len(base) + 1))
          
      return base[-1] + x
