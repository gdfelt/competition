#!/usr/bin/env python3

"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

import math

def main():
	size = 20

	print(int((math.factorial(2*size))/(math.factorial(size) * math.factorial(size))))

if __name__ == "__main__":
	main()