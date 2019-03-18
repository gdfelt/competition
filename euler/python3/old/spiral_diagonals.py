#!/usr/bin/env python3

def calc_sum(num):
	s = 0
	for x in range(4):
		s += (num * num - x*(num - 1))
	return s

def main():
	diag_sum = 1
	for i in range(3, 1001+1, 2):
		diag_sum += calc_sum(i)

	print(diag_sum)

if __name__ == "__main__":
	main()