#!/usr/bin/env python3

"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import utils

def sum_of_pd(num):
	s = 0
	for x in utils.fact(num)[:-1]:
		s += x
	return s

def main():
	amicable_list = []

	for x in range(2, 10000):
		pd1 = sum_of_pd(x)
		pd2 = sum_of_pd(pd1)
		if x == pd2 and x != pd1:
			amicable_list.append(x)
	
	amicable_sum = 0
	for n in amicable_list:
		amicable_sum += n
	print(amicable_sum)

if __name__ == "__main__":
	main()