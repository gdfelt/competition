#!/bin/python3

import itertools

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


def main():
	for i in itertools.permutations(range(7, 0, -1)):
		s = int("".join(str(x) for x in i))
		if is_prime(s):
			print(s)
			break

if __name__ == "__main__":
	main()