#!/usr/bin/env python3

import utils




def main():
	
	num_limit = 2000000
	p_sum = 0

	for i in range(2, num_limit):
		if utils.is_prime(i):
			p_sum += i
	print(p_sum)

if __name__ == "__main__":
	main()
