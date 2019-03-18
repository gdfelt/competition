#!/usr/bin/env python3

import utils




def main():
	p_count = 0
	num = 1
	#for n in range(2, 100):
	while p_count < 10001:
		num +=1
		if utils.is_prime(num):
			p_count+=1
	
	print('count: ' + str(p_count) + ' prime value: ' + str(num))


if __name__ == "__main__":
	main()