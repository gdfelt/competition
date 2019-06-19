#!/usr/bin/env python3

"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

import utils

def main():
	sum_set = set()
	for x in range(2000,10000):
		s = str(x)
		if len(set(s)) == len(s) and '0' not in s:
			fact_list = utils.get_factors(x)[1:-1]
			for i,f in enumerate(fact_list[:len(fact_list)//2]):
				tmp = str(fact_list[i]) + str(fact_list[len(fact_list) - i -1]) + s
				if len(tmp) == 9 and len(set(tmp)) == len(tmp) and '0' not in tmp:
					sum_set.add(x)

	print(sum(sum_set))

if __name__ == "__main__":
	main()