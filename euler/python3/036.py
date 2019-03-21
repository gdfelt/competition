#!/usr/bin/env python3

"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

import utils

def main():
	running_sum = 0
	for x in range(1, 1000000):
		if utils.is_palindrome(x) and utils.is_palindrome('{0:b}'.format(x)):
			running_sum += x
	print(running_sum)

if __name__ == "__main__":
	main()