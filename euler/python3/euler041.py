#!/usr/bin/env python3

"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools
import utils

def main():
	for i in itertools.permutations(range(7, 0, -1)):
		s = int("".join(str(x) for x in i))
		if utils.is_prime(s):
			print(s)
			break

if __name__ == "__main__":
	main()