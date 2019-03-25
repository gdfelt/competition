#!/usr/bin/env python3

"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import utils

def check_right(num):
	if num == '': return True
	n = int(num)
	if not utils.is_prime(n):
		return False
	return check_right(str(n)[1:])

def check_left(num):
	if num == '': return True
	n = int(num)
	if not utils.is_prime(n):
		return False
	return check_left(str(n)[:-1])

def main():
	running_sum = 0
	for index, b in enumerate(utils.get_prime_sieve(1000000)):
		if b and index > 10 and check_right(str(index)) and check_left(str(index)):
			running_sum += index
	print(running_sum)

if __name__ == "__main__":
	main()