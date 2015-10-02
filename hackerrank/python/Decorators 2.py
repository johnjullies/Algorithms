# https://www.hackerrank.com/challenges/decorators-2-name-directory/

def outer(function):
    def inner(ls):
        return sorted([function(l) for l in ls], key=lambda x: x[-2])
    return inner

@outer
def compute(ls):
    return [["Mr."], ["Ms."]][ls[-1] != "M"] + ls

if __name__ == "__main__":
    ls, n = [], int(input())
    
    for _ in range(n):
        ls.append(input().split())

    for l in compute(ls):
        print(" ".join(l[:-2]))