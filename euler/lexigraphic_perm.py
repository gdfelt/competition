#!/usr/bin/env python3

import itertools

def main():
	count = 0
	for perm in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
		count += 1
		if count == 1000000:
			print(perm)
			break


if __name__ == "__main__":
	main()