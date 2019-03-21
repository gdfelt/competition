#!/usr/bin/env python3

"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

import math
import functools

@functools.lru_cache(maxsize=None)
def quint_pow(num):
	if num == 0: return 0
	if num == 1: return 1
	return math.pow(num, 5)

def main():
	pow_sum = 0
	for x in range(2, 1000000):
		s = str(x)
		sum_digits = 0
		for c in s:
			sum_digits += quint_pow(int(c))
		if sum_digits == x:
			pow_sum += x
	print(pow_sum)

if __name__ == "__main__":
	main()