#!/usr/bin/env python3

"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import utils

sieve = utils.get_prime_sieve(1000000)

def check_rotation_list(list_rotations):
	for r in list_rotations:
		if sieve[int(r)] == False:
			return False
	return True

def get_rotations(str):
	rotations = []
	for x in range(len(str)):
		rotations.append(str[x:] + str[0:x])
	#print(rotations)
	return rotations

def main():
	count = 0
	for index, n in enumerate(sieve):
		if n == True:
			if check_rotation_list(get_rotations(str(index))):
				count += 1
	print(count)
			

if __name__ == "__main__":
	main()