#!/usr/bin/env python3

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
	with open('p067_triangle.dat') as file:
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