#!/usr/bin/env python3

import functools

def get_prime_sieve(up_limit):
    sieve = [True] * up_limit
    sieve[0] = sieve[1] = False

    for (i, isprime) in enumerate(sieve):
        #print(i)
        if isprime:
          #  yield i
            for n in range(i*i, up_limit, i):
                sieve[n] = False
    #print(sieve)
    return list(sieve)


def is_prime(n):
    """"pre-condition: n is an integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2: return False
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    
    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0: return False
        i += w
        w = 6 - w
    return True


@functools.lru_cache(maxsize=None)
def fact( num ):
    fact_list = sorted(set(functools.reduce(list.__add__,([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0))))
    return fact_list