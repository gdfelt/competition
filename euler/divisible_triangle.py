#!/usr/bin/env python3

import utils

def main():
	run_sum = 0
	index = 0
	fact_count = 0
	while fact_count < 500:
		index += 1
		run_sum += index
		fact_count = len(utils.fact(run_sum))
	
	print(str(index) + ': ' + str(run_sum) + ' fc: ' + str(fact_count))

if __name__ == "__main__":
	main()
