from primefunctions import factors


def prime_list(n: int) -> dict:
    ret = {}
    facs = factors(n)
    for i in facs:
        ret[i] = facs.count(i)
    return ret


def main():
    max_primes = {}
    for i in range(1,21):
        prime_l = prime_list(i)
        for prime, prime_total in prime_l.items():
            # print(prime)
            if not prime in max_primes:
                max_primes[prime] = prime_total
            elif prime_total > max_primes[prime]:
                max_primes[prime] = prime_total
    
    prod = 1
    for prime, prime_total in max_primes.items():
        prod*=prime ** prime_total
    print(prod)

if __name__ == "__main__":
    main()
