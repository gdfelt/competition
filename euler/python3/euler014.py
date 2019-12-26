#!/usr/bin/env python3

"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import functools

max_num = 1000000

@functools.lru_cache(maxsize=None)
def get_next_value(num):
	if num % 2 == 0:
		return num / 2
	else:
		return num * 3 + 1

def get_collatz(num):
	count = 1
	not_end = True
	tmp = num
	while not_end:
		tmp = get_next_value(tmp)
		count += 1
		if tmp == 1:
			not_end = False
	return count

def main():
	max_count = 0
	max_value = 0
	for i in range(max_num // 2, max_num):
		tmp_count = get_collatz(i)
		if tmp_count > max_count:
			max_count = tmp_count
			max_value = i

	print(str(max_value))

if __name__ == "__main__":
	main()
