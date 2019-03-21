#!/usr/bin/env python3

"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import utils

def main():
	running_sum = 0
	for x in range(3, 1000000):
		s = str(x)
		sum_fact = 0
		for c in s:
			sum_fact += utils.get_factorial(int(c))
		if sum_fact == x:
			running_sum += x
	print(running_sum)

if __name__ == "__main__":
	main()