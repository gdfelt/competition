#!/usr/bin/env python3

import functools

def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True


@functools.lru_cache(maxsize=None)
def fact( num ):
    fact_list = sorted(set(functools.reduce(list.__add__,([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0))))
    return fact_list