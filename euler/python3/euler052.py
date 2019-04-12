#!/usr/bin/env python3

"""
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

import utils

def main():
	#limit = 1000000000
	num_found = False
	x = 1
	while not num_found:
		if len(str(x)) == len(str(6 * x)):
			if (utils.is_permuation(str(x), str(x * 2)) and utils.is_permuation(str(x), str(x * 3)) and 
				utils.is_permuation(str(x), str(x * 4)) and utils.is_permuation(str(x), str(x * 5)) and 
				utils.is_permuation(str(x), str(x * 6))):
				print(x)
				break
		x += 1


if __name__ == '__main__':
	main()	