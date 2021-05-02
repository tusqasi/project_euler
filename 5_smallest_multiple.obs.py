# 5smallest_multiple.obs.py#
#            OBS           #
from primefunctions import * 
from math import sqrt

def occurs(n, lst):
    """How many times does n occur in lst"""

    c = 0
    for i in lst:
        if i == n:
            c += 1
    return c
f = []
n = 10 

for i in primes_till(n):

    for x in range(1, n):
        z = True
        if x % i == 0 and x > i:
            f.append( x // i)
            z = False
    if z:
        f.append(i)

# print(f)
# o = []
# for i in f:
#     if is_prime(i):
#         o.append(i)
# a = o

a = []

for z in f:
    if z in primes_till(n):
        a.append(z)

print(a)

v = []


for w in a:
    v.append([w, occurs(w, a)])


q = []
for x, w in zip(iter(dict(v)),iter(dict(v).values())):
    q.append(x**w)
c = 1
for i in q:
    c*=i
print(q)
print(c)
***-->