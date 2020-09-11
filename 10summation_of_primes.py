# 10summation_of_primes.py
# solved
# 142913828922
from primefunctions import primes_till

n = 2_000_000 # 2 million

c = 0
primes_till_n = primes_till(n)

for a_prime in primes_till_n:
    c+=a_prime
print(c)
