#!/usr/bin/env python3

"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

import utils

def main():
	p_count = 0
	num = 1
	while p_count < 10001:
		num +=1
		if utils.is_prime(num):
			p_count+=1
	print(str(num))

if __name__ == "__main__":
	main()