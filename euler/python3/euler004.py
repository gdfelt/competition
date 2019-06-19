#!usr/bin/env python3

"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import utils

top_limit = 998001 # Answer won't exceed this
low_limit = 10000

def check_factors(num):
	fact_list = utils.get_factors(num)
	for index, fp in enumerate(fact_list):
		if len(str(fp)) == 3 and len(str(fact_list[len(fact_list) - index - 1])) == 3:
			return True

def main():
	for i in range(top_limit, low_limit, -1):
		if utils.is_palindrome(i):
			if check_factors(i):
				print(i)
				break

if __name__ == "__main__":
	main()