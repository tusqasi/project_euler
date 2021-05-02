# 5smallest_multiple.py
from primefunctions import * 
from math import sqrt

def occurs(n, lst):
    """How many times does n occur in lst"""

    c = 0
    for i in lst:
        if i == n:
            c += 1
    return c
