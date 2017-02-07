def answer(l):
    divs = [0] * len(l)

    for i in xrange(len(l)):
        for j in xrange(i + 1, len(l)):
            if l[j] % l[i] == 0:
                divs[j] += 1

    count = 0
    for i in xrange(len(l) - 1, 1, -1):
        for j in xrange(i - 1, 0, -1):
            if l[i] % l[j] == 0:
                count += divs[j]

    return count
