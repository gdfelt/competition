#!/usr/bin/env python3

"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import utils

def main():
	
	num_limit = 2000000
	p_sum = 0

	for i in range(2, num_limit):
		if utils.is_prime(i):
			p_sum += i
	print(p_sum)

if __name__ == "__main__":
	main()