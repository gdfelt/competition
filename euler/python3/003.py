#!/usr/bin/env python3

"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import utils

def main():
	target = 600851475143
	fac_list = utils.fact(target)
	for f in reversed(fac_list):
		if utils.is_prime(f):
			print(f)
			break

if __name__ == "__main__":
	main()