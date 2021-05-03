import time

def one():
    for c in range(500,0,-1):
        for b in range(500,0,-1):
            for a in range(500,0,-1):
                if a<b<c and a*a + b*b == c*c and a+b+c == 1000:
                    print(a*b*c)
                    return 0
def two():
    for c in range(500,0,-1):
        for b in range(500,0,-1):
            for a in range(500,0,-1):
                if a<b<c and a*a + b*b == c*c and a+b+c == 1000:
                    print(a*b*c)
                    return 0
now = time.time()
one()
print(time.time() - now)
two()
print(time.time() - now)
