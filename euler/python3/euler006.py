#!/usr/bin/env python3

"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def main():
	sum_sqr = 0
	sqr_sum = 0
	for x in range(1, 100+1):
		sum_sqr += x
		sqr_sum += x ** 2
	sum_sqr = sum_sqr ** 2
	print(sum_sqr - sqr_sum)

if __name__ == "__main__":
	main()