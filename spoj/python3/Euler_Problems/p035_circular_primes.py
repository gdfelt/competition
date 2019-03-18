#!/usr/bin/env python3

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