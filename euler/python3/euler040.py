#!/usr/bin/env python3

"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

def main():
	target = [[1, -1], [10, -1], [100, -1], [1000, -1], [10000, -1], [100000, -1], [1000000, -1]]
	index = 0
	for n in range(1, 1000000):
		s = str(n)
		index += len(s)
		for t in target:
			if index - len(s) + 1 <= t[0] and index >= t[0]:
				dif = index - t[0]
				t[1] = int(s[::-1][dif])
	run = 1
	for t in target:
		run *= t[1]
	print(run)

if __name__ == '__main__':
	main()
