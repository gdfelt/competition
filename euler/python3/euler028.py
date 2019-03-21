#!/usr/bin/env python3

"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

def calc_sum(num):
	s = 0
	for x in range(4):
		s += (num * num - x*(num - 1))
	return s

def main():
	diag_sum = 1
	for i in range(3, 1001+1, 2):
		diag_sum += calc_sum(i)
	print(diag_sum)

if __name__ == "__main__":
	main()