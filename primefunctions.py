# primefunction.py

from math import sqrt

def is_prime(n):
    """ Check's if the given number is a prime. 

    If a list is passed each number is replaced by bools in place

    Simple checking for prime
    """

    # Checks if given a list...
    if type(n) == list:
        if_prime_list = [False, ] * len(n)
        c = 0
        for i in n:
            if PrimeFunctions.is_prime(i):
                if_prime_list[c] = True
            c += 1
        # and returns one with weather or not it's prime in place
        return if_prime_list

    # When a single number ..

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    """ Returns the nth prime """
    """ uses seive of someone"""

    head_number = 1
    the_prime = 2

    while head_number <= n:
        # Adds to the_prime till a prime is reached
        # When a prime is reached head move ahead.

        if is_prime(the_prime):
            head_number += 1
        the_prime += 1

        # Go use the Debugger if confused.
    return the_prime-1

def primes_till(n):
    """Gives primes till the given number

    Args:
        n (int): Then number upto which primes are calulated

    Returns:
        list: A list of prime upto n
    """    


    n = int(n)
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True,] * (n+1)
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    primes = []
    for i in range(n):
        if prime[i]:
            primes.append(i)
    
    return primes

def factors(n):
    """Factorizes given number

    Args:
        n (int): This numbers is factorized

    Returns:
        A list of prime Factors of the given number

    """

    factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n /= 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(n))+1, 2):

        # while i divides n, print i ad divide n
        while n % i == 0:
            factors.append(int(i))

            n /= i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(int(n))
    return factors


def prime_before(n):
    """Gives prime before the given number

    Args:
        n (int): the number below which the prime is needed

    Returns:
        int: the prime before n
    """    

    for i in range(n, int(sqrt(n)), -1):
        if is_prime(i): return i


# testing code below

