#!/usr/bin/env python3

"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def main():
	s = '0b1' + '0' * 1000
	total = 0
	for c in str(int(s, 2)):
		total += int(c)
	print(total)

if __name__ == "__main__":
	main()