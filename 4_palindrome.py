def palidrome(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != n[len(n) - i -1]:
            return 0 

    return 1
nm = set()
for i in range(100,1000):
    for j in range(i,1000):
        if palidrome(i*j):
            nm.add(i*j)

print(max(nm))
