#!/usr/bin/env python3

"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

def main():
	prod = 1
	for x in range(1, 100):
		prod *= x
	s = 0
	for c in str(prod):
		s += (int(c))
	print(s)

if __name__ == "__main__":
	main()