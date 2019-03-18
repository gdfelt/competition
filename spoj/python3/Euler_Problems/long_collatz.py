#!/bin/python3

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
	#print(num)
	tmp = num
	while not_end:
		tmp = get_next_value(tmp)
		#print(tmp)
		count += 1
		if tmp == 1:
			not_end = False

	#print('value: ' + str(num) + ' count: ' + str(count))
	return count

def main():
	max_count = 0
	max_value = 0
	for i in range(2, max_num):
		tmp_count = get_collatz(i)
		if tmp_count > max_count:
			max_count = tmp_count
			max_value = i

	print('Max value is ' + str(max_value) + ' count is ' + str(max_count))

if __name__ == "__main__":
	main()