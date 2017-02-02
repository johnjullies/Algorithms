def answer(l):
    q0=[]
    q1=[]
    q2=[]
    
    l.sort()
    sums = sum(l)
    
    for i in l:
        if (i % 3) == 0:
            q0.insert(0, i)
        if (i % 3) == 1:
            q1.insert(0, i)
        if (i % 3) == 2:
            q2.insert(0, i)
            
    if sums % 3 == 1:
        if len(q1):
            q1.pop()
        elif len(q2) >= 2:
            q2.pop()
            q2.pop()
        else:
            return 0
    elif sums % 3 == 2:
        if len(q2):
            q2.pop()
        elif len(q1) >=2:
            q1.pop()
            q1.pop()
        else:
            return 0
    
    q0.extend(q1)
    q0.extend(q2)
    
    if len(q0) <= 0:
        return 0
        
    q0.sort()
    q0.reverse()
    
    result = ''.join(str(x) for x in q0)
    
    return int(result)
