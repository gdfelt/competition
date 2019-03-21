#!/usr/bin/env python3

"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

def get_max_sum(up_num, low_num_left, low_num_right):
	if low_num_left > low_num_right:
		return up_num + low_num_left
	return up_num + low_num_right

def calc_sum_list(upper_list, lower_list):
	tmp_set = []
	for ind, n in enumerate(upper_list):
		tmp_set.append(get_max_sum(n, lower_list[ind], lower_list[ind + 1]))
	return tmp_set

def main():
	with open('resources/triangle.txt') as file:
		num_lines = sum(1 for line in file)
		file.seek(0)
		running_list = []
		# initialize bottom row (first running list)
		for ind, l in enumerate(file, start=1):
			if ind == num_lines:
				running_list = [int(n) for n in l.split()]
		file.seek(0)

		for index in range(num_lines-1, 0, -1):
			cur_list = []
			file.seek(0)
			for ind, l in enumerate(file, start=1):
				if ind == index:
					cur_list = [int(n) for n in l.split()]
					break
			running_list = calc_sum_list(cur_list, running_list)
		print(running_list[0])

if __name__ == "__main__":
	main()
